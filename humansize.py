SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximateSize(size , a_kilobyte_is_1024_bytes = True):
    '''
    Convert a file size in human readable form

        Keyword Arguments:
        size -- file size in bytes
        a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                    if False, use multiples of 1000

        Returns : string
    '''
    if size < 0:
        raise ValueError("Must be a positive integer")

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size = size/multiple

        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError("Value is too large")


if __name__ == '__main__' :
    print approximateSize(1000000000000 , False)
    print approximateSize(1000000000000)
