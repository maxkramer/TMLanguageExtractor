import glob
import os
import shutil 
import zipfile


subl_path = raw_input("Please enter the path to Sublime Text 2.app: ")
subl_path = subl_path.replace('\\', '').strip()
                                                                               
files_path = subl_path + '/Contents/MacOS/Pristine Packages/*.sublime-package'
files = glob.glob(files_path)

output_dir = os.path.expanduser('~/Desktop/TMLanguages/')
tmp_dir = '/tmp/tmlang_zips/'

if len(files) > 0:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    os.makedirs(tmp_dir)

    for fp in files:
        fn = os.path.basename(os.path.normpath(fp))

        zfile = zipfile.ZipFile(fp)
        zfile.extractall(tmp_dir + fn)

        languages = glob.glob(tmp_dir + fn + '/*.tmLanguage')
        if len(languages) > 0:
            for lang in languages:
                without_ext = fn.replace(".sublime-package", "")
                print 'Found ' + without_ext
                shutil.move(lang, output_dir)

        print 'Cleaning up'
        shutil.rmtree(tmp_dir)
        print 'All done'

    os.system('open ' + output_dir)
else:
    print 'No files exist in ' + files_path