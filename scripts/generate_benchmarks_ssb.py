import os
from python_helpers import open_utf8


def format_ssb_queries(target_dir, ssb_in, comment, sf):
    with open_utf8(ssb_in, 'r') as f:
        text = f.read()

    for i in [11, 12, 13, 21, 22, 23, 31, 32, 33, 34, 41, 42, 43]:
        qnr = '%02d' % (i,)
        target_file = os.path.join(target_dir, 'q' + qnr + '.benchmark')
        new_text = '''# name: %s
# description: Run query %02d from the SSB benchmark (%s)
# group: [sf%d]

template %s
SCALING_FACTOR=%d
QUERY_NUMBER=%d
QUERY_NUMBER_PADDED=%02d''' % (
            target_file,
            i,
            comment,
            sf,
            ssb_in,
            sf,
            i,
            i,
        )
        with open_utf8(target_file, 'w+') as f:
            f.write(new_text)


# generate the TPC-H benchmark files
ssb_folder = os.path.join('benchmark', 'ssb')
in_file = os.path.join(ssb_folder, 'ssb.benchmark.in')

for sf in [1, 10, 100]:
    dir = os.path.join(ssb_folder, f'sf{sf}')
    format_ssb_queries(dir, in_file, 'single-threaded', sf)
