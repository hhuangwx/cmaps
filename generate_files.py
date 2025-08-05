#!/usr/bin/env python
"""
File generation script - extracted logic from setup.py
Used to generate _version.py and cmaps.py files
"""

from glob import glob
import os

CMAPSFILE_DIR = os.path.join('./cmaps/colormaps')


def _listfname():
    """Get colormap file list"""
    l = {}

    l.update({'ncl': {
        'p': 'os.path.join(CMAPSFILE_DIR, "ncar_ncl", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'ncar_ncl/*.rgb')))}})
    l.update({'self_defined': {
        'p': 'os.path.join(CMAPSFILE_DIR, "self_defined", ',
        'l': sorted(glob(os.path.join(CMAPSFILE_DIR, 'self_defined/*.rgb')))}})

    return l


def write_cmaps(template_file='./cmaps.template'):
    """Generate cmaps.py file"""
    print(f"Generating cmaps.py from template: {template_file}")
    
    if not os.path.exists(template_file):
        print(f"❌ Template file not found: {template_file}")
        return
        
    with open(template_file, 'rt') as f:
        c = f.read()
    
    l = _listfname()
    for t in l.keys():
        for cmap_file in l[t]['l']:
            cname = os.path.basename(cmap_file).split('.rgb')[0]
            # start with the number will result illegal attribute
            if cname[0].isdigit() or cname.startswith('_'):
                cname = 'N' + cname
            if '-' in cname:
                cname = 'cmaps_' + cname.replace('-', '_')
            if '+' in cname:
                cname = 'cmaps_' + cname.replace('+', '_')
            c += '    @property\n'
            c += '    def {}(self):\n'.format(cname)
            c += '        cname = "{}"\n'.format(cname)
            c += '        try:\n'
            c += '            return get_cmap(cname)\n'
            c += '        except:\n'
            c += '            cmap_file = {} "{}")\n'.format(l[t]['p'], os.path.basename(cmap_file))
            c += '            cmap = Colormap(self._coltbl(cmap_file), name=cname)\n'
            c += '            register_cmap(name=cname, cmap=cmap)\n'
            c += '            return cmap\n\n'

            c += '    @property\n'
            c += '    def {}(self):\n'.format(cname + '_r')
            c += '        cname = "{}"\n'.format(cname + '_r')
            c += '        try:\n'
            c += '            return get_cmap(cname)\n'
            c += '        except:\n'
            c += '            cmap_file = {} "{}")\n'.format(l[t]['p'], os.path.basename(cmap_file))
            c += '            cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)\n'
            c += '            register_cmap(name=cname, cmap=cmap)\n'
            c += '            return cmap\n\n'

    cmapspy = './cmaps/cmaps.py'
    with open(cmapspy, 'wt') as fw:
        fw.write(c)


def main():
    """Main function: generate all necessary files"""
    print("🔧 Starting file generation...")
    
    # Ensure directory exists
    os.makedirs('cmaps', exist_ok=True)
    
    # Generate cmaps.py file
    write_cmaps()
    print("✅ Cmaps file generated")
    
    print("🎉 File generation completed successfully!")


if __name__ == '__main__':
    main()
