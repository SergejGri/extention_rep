from os import rename
from os import path
from os import listdir


class Extention_rep:
    def __init__(self, dir_to_source, old_ext, new_ext):
        self.dir_to_source = dir_to_source
        self.old_ext = old_ext
        self.new_ext = new_ext
        if self.new_ext == None:
            print('Can not replace extentions. New extention was not passed.')
        elif self.old_ext == None:
            print('Can not replace extentions. Extention which is ment to be replaced was not passed.')
        elif self.old_ext == None and self.new_ext == None:
            print('Can not replace extentions. Neither the new nor the old '
                  'extention which is ment to be replaced were not passed.')
        else:
            pass

    def extention(self):
        file_count = 0
        try:
            for file in listdir(self.dir_to_source):
                if file.endswith(self.old_ext):
                    name = path.splitext(str(file))[0]
                    rename(self.dir_to_source + name + self.old_ext,
                              self.dir_to_source + name + self.new_ext)
                    file_count += 1
                else:
                    pass

        except FileNotFoundError:
            print('Could not open files. Please check root directory.')
        print(f'Done! {file_count} files were renamed.')

    def arb_sign(self):
        file_count = 1
        try:
            for file in listdir(self.dir_to_source):
                self.old_ext = self.dot_check()
                self.new_ext = self.dot_check()
                if file.endswith(self.old_ext):
                    name = path.splitext(str(file))[0]
                    rename(self.dir_to_source + name + self.old_ext,
                            self.dir_to_source + name + self.new_ext)
                else:
                    pass
                file_count += 1
        except FileNotFoundError:
            print('Could not open files. Please check root directory.')
        print(f'Done! {file_count} files were renamed.')

    def dot_check(self, string):
        if string.find('.'):
            return string
        else:
            return rename(string, '.' + string)


def main():
    dir = r'' # place our working directory here
    replace = Extention_rep(dir_to_source=dir, old_ext='.mp4', new_ext='.jpg')
    replace.extention()

if __name__ == '__main__':
    main()


