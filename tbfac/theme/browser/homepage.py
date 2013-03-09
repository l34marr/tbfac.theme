from zope.interface import implements
from zope.component import getMultiAdapter
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

from tbfac.theme.browser.interfaces import IHomepage


class Homepage(BrowserView):
    
    implements(IHomepage)
    
    def fixed_items(self):
        """ Get Items for Fixed-Position Tiles
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/fixed'
        return catalog(portal_type='tbfac.Advert',
                       review_state='published',
                       path=path,
                       sort_on='getObjPositionInParent',
                       sort_order='ascending',
                       sort_limit=9)[:9]

    def info_items(self):
        """ Get Items for Info Tiles
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request),
            name=u'plone_portal_state')
        path = portal_state.navigation_root_path() + '/event/info'
        return catalog(portal_type='tbfac.Info',
                       review_state='published',
                       path=path,
                       sort_on='created',
                       sort_order='descending',
                       sort_limit=12)[:12]

    def latest_review(self, name):
        """ Return Jury's Latest Review
        """

