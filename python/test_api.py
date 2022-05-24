import dropbox
import os

TOKEN = os.environ.get('TOKEN')

dbx = dropbox.Dropbox('TOKEN')
# dbx = dropbox.Dropbox("sl.BH1itfAslyMj3fnQnL9U9dxiDlp8dY9-z-sdcx4otdzwOAr5XFGiF5HbnDJ_DYlOOu4RQUvYJ2_ddR4lUtege0HvA7v-3QWFKcX-Mbk37B3fI3H9kBbsNjFEREScJMZ5oRyEKEs")

SOURCE = '/automagic_dropsave/source/'
DEST = '/automagic_dropsave/destination/'



dbx.users_get_current_account()

for entry in dbx.files_list_folder('').entries:
    print(entry.name)
