import os
import django
import random
os.environ['DJANGO_SETTINGS_MODULE'] = 'reporting_platform.settings'
django.setup()
from django.conf import settings
if not settings.configured:
    settings.configure(DEFAULT_INDEX_TABLESPACE='')

from django.contrib.auth.models import User
from dashboard.models import Post

text_list = ["Lorem ipsum dolor sit amet, mea an homero commodo contentiones. Autem probatus sapientem in vis, ad paulo minimum his. Vel feugait noluisse an, eos graeco pertinacia neglegentur eu. Prima clita salutatus in vim.",
"Sed amet torquatos cu, est id summo dicit. Has ne dignissim similique, timeam platonem ut vis. Graeci fierent vix ad, eos elitr iracundia in. Mel tamquam aliquam consulatu ne, mel at elitr percipit. Doctus propriae interesset ad cum. ",
"Est dicta sonet semper in. Cum facilis corrumpit urbanitas an, legimus ancillae sententiae mei ut. Volumus cotidieque vis at, populo labore no eum. Id pri eros malorum, cu illum quando dicant qui, pro ad omnes soluta. Dico primis democritum an vel, est viris persequeris an. Vel ea veniam partem sadipscing, vis ei eripuit invenire.",
"Id pri possim invidunt, mucius graeco sadipscing ius eu. Integre deseruisse dissentias mel an, dolor elaboraret ne eam. Ex pri case sale dicant, an mea aliquam quaestio iracundia, consulatu adipiscing nam at. Stet dicta luptatum mea eu, ex mutat decore eam, pro cu everti utroque alienum.",
"Vis mutat iusto putent no, no nec omnis mutat labore. Duo dicunt nominavi explicari id, ut sumo erroribus mea, adhuc iusto intellegebat an vim. Et pertinax disputando vel. Congue sensibus mediocritatem ut cum, idque putant graecis an nam.",
"Ad qui docendi phaedrum, gloriatur reformidans eum no, iusto delenit aliquando ea eam. At minim nullam ius, dico graeci his ut. Ad facer impedit ancillae cum, putant vivendo cotidieque at nam."]


for i in range(0, 10):
    x = random.randint(0, 5)
    user = User.objects.get(username='admin')
    title = "Post %d ABC" % (i)
    a = Post.objects.create(author=user, title=title, content=text_list[x])
    a.publish()
    a.save()

