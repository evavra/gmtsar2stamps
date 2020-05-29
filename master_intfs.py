import sys
import glob
import subprocess


def main():
    """
    Make all possible interferograms with master scene.
    Run in slc directory and specify master.PRM at command line.
    Example: master_intfs.py S1_20170905_ALL_F2.PRM
    """

    # First, check for topo_ra.grd
    if len(glob.glob('topo_ra.grd')) < 1:
        print('topo_ra.grd needs to be saved or linked in current directory!')
        return

    # Get list of PRMs
    prms = glob.glob('*PRM')
    prms.sort()

    # Assign master from arguments
    supermaster = sys.argv[1]

    # Get index of supermaster in list
    m = prms.index(supermaster)

    # Loop through all
    for i, PRM in enumerate(prms):
        if i < m:
            # print('intf.csh {} {} -topo topo_ra.grd'.format(PRM, supermaster))
            print('Working on {} of {}'.format(i+1, len(prms)-1))
            subprocess.call('intf.csh {} {} -topo topo_ra.grd'.format(PRM, supermaster), shell=True)
        elif i == m:
            continue
        elif i > m:
            # print('intf.csh {} {} -topo topo_ra.grd'.format(supermaster, PRM))
            print('Working on {} of {}'.format(i, len(prms)-1))
            subprocess.call('intf.csh {} {} -topo topo_ra.grd'.format(supermaster, PRM), shell=True)


if __name__ == '__main__':
    main()
