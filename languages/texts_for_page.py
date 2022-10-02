"""
Texts for our pages
"""
from django.utils.translation import gettext as _

#texts for home page
texts_for_home = []#

#navbar
language = _('Language')
texts_for_home.append(language)

home = _('Home')
texts_for_home.append(home)

#bodu
card_header = _('Warsaw')
texts_for_home.append(card_header)

card_title = _('Warsaw officially the Capital City of Warsaw')
texts_for_home.append(card_title)

card_text1 = _("""
Is the capital and largest city of Poland. The metropolis stands on the River Vistula in east-central Poland,
and its population is officially estimated at 1.8 million residents within a greater metropolitan area of 3.1 million residents,
which makes Warsaw the 7th most-populous capital city in the European Union.
The city area measures 517 km2 (200 sq mi) and comprises 18 quarters, while the metropolitan area covers 6,100 km2 (2,355 sq mi).
Warsaw is an Alpha global city,[7] a major cultural, political and economic hub, and the country's seat of government.
""")
texts_for_home.append(card_text1)

card_text2 = _("""
Warsaw traces its origins to a small fishing town in Masovia.
The city rose to prominence in the late 16th century,
when Sigismund III decided to move the Polish capital and his royal court from Kraków.
Warsaw served as the de facto capital of the Polish–Lithuanian Commonwealth until 1795, and subsequently as the seat of Napoleon's Duchy of Warsaw.
The 19th century and its Industrial Revolution brought a demographic boom which made it one of the largest and most densely-populated cities in Europe.
Known then for its elegant architecture and boulevards, Warsaw was bombed and besieged at the start of World War II in 1939.
Much of the historic city was destroyed and its diverse population decimated by the Ghetto Uprising in 1943, the general Warsaw Uprising in 1944 and systematic razing.
""")
texts_for_home.append(card_text2)

footer = _('copied from')
texts_for_home.append(footer)

"""
2 method:

texts_for_home = {
    'language': _('Language'),
    'home': _('Home'),
    'card_header': _('Warsaw'),
    'card_title': _('Warsaw officially the Capital City of Warsaw'),
}
"""