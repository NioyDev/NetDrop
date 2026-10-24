DOCUMENTS = {
    'txt', 'pdf', 'doc', 'docx', 'docm', 'dot', 'dotx', 'odt', 'ott', 'rtf', 'md', 'markdown',
    'tex', 'log', 'wpd', 'wps', 'pages', 'xps', 'oxps', 'djvu', 'epub', 'mobi', 'azw', 'azw3',
    'fb2', 'cbz', 'cbr', 'pub', 'vsd', 'vsdx', 'one', 'rst', 'nfo', 'text'
}

SPREADSHEETS_PRESENTATIONS = {
    'xls', 'xlsx', 'xlsm', 'xlsb', 'xlt', 'xltx', 'ods', 'ots', 'csv', 'tsv', 'numbers',
    'ppt', 'pptx', 'pptm', 'pps', 'ppsx', 'pot', 'potx', 'odp', 'otp', 'key'
}

IMAGES = {
    'png', 'jpg', 'jpeg', 'jpe', 'jfif', 'gif', 'webp', 'heic', 'heif', 'avif', 'bmp', 'dib',
    'tiff', 'tif', 'svg', 'svgz', 'ico', 'icns', 'cur', 'tga', 'pcx', 'ppm', 'pgm', 'pbm',
    'psd', 'psb', 'ai', 'eps', 'indd', 'xcf', 'kra', 'sketch', 'fig', 'xd', 'afdesign',
    'afphoto', 'cdr', 'jp2', 'j2k', 'jxl', 'exr', 'hdr', 'apng',
    # RAW de cámaras
    'raw', 'cr2', 'cr3', 'crw', 'nef', 'nrw', 'arw', 'srf', 'sr2', 'dng', 'orf', 'rw2',
    'raf', 'pef', 'srw', '3fr', 'x3f', 'rwl', 'mrw'
}

AUDIO = {
    'mp3', 'wav', 'aac', 'm4a', 'm4b', 'opus', 'ogg', 'oga', 'flac', 'wma', 'aiff', 'aif',
    'aifc', 'amr', 'awb', 'mid', 'midi', 'ape', 'wv', 'ac3', 'dts', 'mka', 'ra', 'caf',
    'au', 'snd', '3ga', 'weba', 'm3u', 'm3u8', 'pls', 'cue', 'mod', 'xm', 'it', 's3m'
}

VIDEO = {
    'mp4', 'mov', 'avi', 'mkv', 'webm', 'wmv', 'flv', 'f4v', 'm4v', 'mpg', 'mpeg', 'mpe',
    '3gp', '3g2', 'ts', 'mts', 'm2ts', 'vob', 'ogv', 'asf', 'rm', 'rmvb', 'divx', 'qt',
    'mxf', 'dv', 'swf'
}

SUBTITLES = {'srt', 'vtt', 'ass', 'ssa', 'sub', 'sbv', 'idx', 'lrc'}

ARCHIVES = {
    'zip', 'rar', '7z', 'tar', 'gz', 'tgz', 'bz2', 'tbz2', 'xz', 'txz', 'lz', 'lzma', 'z',
    'zst', 'cab', 'arj', 'lzh', 'iso', 'img', 'dmg', 'vhd', 'vhdx', 'vmdk'
}

CODE = {
    'py', 'pyw', 'ipynb', 'js', 'mjs', 'cjs', 'jsx', 'ts', 'tsx', 'html', 'htm', 'xhtml',
    'css', 'scss', 'sass', 'less', 'vue', 'svelte', 'astro',
    'java', 'class', 'kt', 'kts', 'scala', 'groovy', 'gradle',
    'c', 'h', 'cpp', 'cc', 'cxx', 'hpp', 'hh', 'cs', 'vb', 'fs', 'go', 'rs', 'swift', 'm', 'mm',
    'php', 'rb', 'pl', 'pm', 'lua', 'r', 'jl', 'dart', 'ex', 'exs', 'erl', 'hs', 'clj', 'cljs',
    'lisp', 'el', 'ml', 'nim', 'zig', 'v', 'asm', 's', 'f', 'f90', 'cob', 'pas', 'd',
    'sql', 'sqlite', 'db', 'mdb', 'accdb', 'psql',
    'sh', 'bash', 'zsh', 'fish', 'ps1', 'psm1', 'bat', 'cmd',
    'makefile', 'cmake', 'dockerfile', 'tf', 'proto', 'graphql', 'gql', 'sol', 'wasm'
}

DATA_CONFIG = {
    'json', 'jsonl', 'ndjson', 'xml', 'xsd', 'xsl', 'xslt', 'yaml', 'yml', 'toml', 'ini',
    'cfg', 'conf', 'env', 'properties', 'plist', 'reg', 'parquet', 'avro', 'orc', 'feather',
    'pkl', 'pickle', 'npy', 'npz', 'h5', 'hdf5', 'mat', 'sav', 'dta', 'rdata', 'rds',
    'geojson', 'kml', 'kmz', 'gpx', 'shp', 'shx', 'dbf', 'bib', 'ris', 'tmx', 'po', 'pot',
    'mo', 'lock', 'map', 'pem', 'crt', 'cer', 'key'
}

FONTS = {'ttf', 'otf', 'woff', 'woff2', 'eot', 'ttc', 'fon', 'pfb'}

MODELS_3D_CAD = {
    'obj', 'stl', 'fbx', 'glb', 'gltf', '3ds', 'dae', 'blend', 'max', 'ma', 'mb', 'c4d',
    'ply', 'usd', 'usdz', '3mf', 'step', 'stp', 'iges', 'igs', 'dwg', 'dxf', 'skp', 'gcode',
    'sldprt', 'sldasm', 'ipt', 'iam', 'rvt', 'ifc', 'fbx'
}

MISC = {
    'vcf', 'ics', 'ical', 'eml', 'msg', 'mbox', 'emlx', 'torrent', 'url', 'webloc', 'lnk',
    'ass', 'sav', 'save', 'rom', 'nes', 'smc', 'gba', 'nds', 'bak', 'tmp', 'old', 'bin', 'dat'
}

# ⚠️ Pueden ejecutar código o instalar software
RISKY = {
    'exe', 'msi', 'apk', 'xapk', 'aab', 'ipa', 'deb', 'rpm', 'pkg', 'appimage', 'snap',
    'flatpak', 'jar', 'war', 'com', 'scr', 'dll', 'sys', 'so', 'dylib', 'vbs', 'vbe',
    'wsf', 'jse', 'hta', 'msp', 'msc', 'gadget', 'app', 'run', 'bundle', 'crx', 'xpi',
    'cpl', 'inf', 'pif'
}

ALLOWED_EXTENSIONS = (
    DOCUMENTS | SPREADSHEETS_PRESENTATIONS | IMAGES | AUDIO | VIDEO | SUBTITLES |
    ARCHIVES | CODE | DATA_CONFIG | FONTS | MODELS_3D_CAD | MISC | RISKY
)
 
MAX_FILE_SIZE = 1000 * 1024 * 1024  # 1GB
