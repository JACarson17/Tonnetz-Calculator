name_to_value: dict[str, int] = {'C':0,
                                 'C#':1,
                                 'D':2,
                                 'D#':3,
                                 'E':4,
                                 'F':5,
                                 'F#':6,
                                 'G':7,
                                 'G#':8,
                                 'A':9,
                                 'A#':10,
                                 'B':11}

value_to_name: dict[int, str] = dict([(value, key) for key, value in name_to_value.items()])

b_to_s_enharm = {'Db':'C#',
                 'Eb':'D#',
                 'Fb':'E',
                 'Gb':'F#',
                 'Ab':'G#',
                 'Bb':'A#',
                 'Cb':'B'}