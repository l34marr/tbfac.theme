from zope.interface import implements

from Products.Five.browser import BrowserView

from tbfac.theme.browser.interfaces import IHomepage


class Homepage(BrowserView):
    
    implements(IHomepage)
    
    def fixed_items(self):
        pass

    def jury_items(self):
        pass

    def info_items(self):
        pass

