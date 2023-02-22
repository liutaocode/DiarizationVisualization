from argparse import ArgumentParser
from scipy.io import wavfile

def get_rttm_dict(rttm_file):
    rttm_dict = dict()
    for line in open(rttm_file).readlines():
        items = line.replace("\n", "").split()
        filename, start_time, duration, spk_name = items[1], float(items[3]), float(items[4]), items[7]
        end_time = start_time + duration

        if spk_name not in rttm_dict.keys():
            rttm_dict[spk_name] = []
        rttm_dict[spk_name].append((start_time,end_time))
    return rttm_dict

def saved_to_text_grid(saved_to_path, current_speaker_num, wav_end_time, spk_dict):
    saved_obj = open(saved_to_path,"w")
    saved_obj.write("File type = \"ooTextFile\"\n")
    saved_obj.write("Object class = \"TextGrid\"\n")
    saved_obj.write("xmin = 0\n")
    saved_obj.write("xmax = %f\n"%(wav_end_time))
    saved_obj.write("tiers? <exists>\n")
    saved_obj.write("size = %d\n"%(current_speaker_num))
    saved_obj.write("item []: \n")

    for i, speaker_id in enumerate(list(spk_dict.keys())):
        saved_obj.write("    item [%d]:\n"%(i))
        saved_obj.write(" \n")
        saved_obj.write("        class = \"IntervalTier\"  \n")
        saved_obj.write("        name = \"%s\"  \n"%(speaker_id))
        saved_obj.write("        xmin = 0  \n")
        saved_obj.write("        xmax = %f  \n"%(wav_end_time))
        intervals = list(spk_dict[speaker_id])
        intervals.sort()

        if len(intervals) == 0:
            saved_obj.write("        intervals: size = 0  \n")
            continue

        all_intervals = []
        if len(intervals) == 1:
            all_intervals.append((0, intervals[0][0], ''))
            all_intervals.append((intervals[0][0], intervals[0][1], 'speech'))
            all_intervals.append((intervals[0][1], wav_end_time, ''))
        else:
            for index, period in enumerate(intervals):
                if index == 0 :
                    all_intervals.append((0, period[0], ''))
                elif index == len(intervals) - 1 :
                    all_intervals.append((period[1], wav_end_time, ''))
                else:
                    all_intervals.append((intervals[index-1][1], period[0], ''))
                all_intervals.append((period[0], period[1], 'speech'))

        saved_obj.write("        intervals: size = %d  \n"%(len(all_intervals)))

        for index, items in enumerate(all_intervals):
            saved_obj.write("        intervals [%d]:\n"%(index))
            saved_obj.write("            xmin = %0.15f \n"%(items[0]))
            saved_obj.write("            xmax = %0.15f \n"%(items[1]))
            saved_obj.write("            text = \"%s\" \n"%(items[2]))


    saved_obj.close()

def main():
    parser = ArgumentParser(
        description='Speaker diarization visualization tool for audio modality.', add_help=True,
        usage='%(prog)s [options]')
    parser.add_argument('-rttm', dest='rttm_fns', help='reference or system RTTM files (default: %(default)s)')
    parser.add_argument('-audio_path', dest='audio_path', help='reference or system audio files (default: %(default)s)')
    parser.add_argument('-praat_result', dest='praat_result_path', help='praat_result_path', default='praat_result.txt')
    args = parser.parse_args()

    rttm_dict = get_rttm_dict(args.rttm_fns)

    sr, audio = wavfile.read(args.audio_path)
    length = audio.shape[0] / sr

    saved_to_text_grid(args.praat_result_path, len(rttm_dict.keys()), length, rttm_dict)

if __name__ == "__main__":
    main()