from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from collective.ckeditor.browser.ckeditorview import CKeditorView as BaseCKeditorView
from zope.component import getMultiAdapter

class CKeditorView(BaseCKeditorView):

    def _isAnonymous(self):
        portal_state = getMultiAdapter(
                (self.context, self.request), name="plone_portal_state")
        if portal_state.anonymous():
            return True
        else:
            return False

    def contentUsesCKeditor(self, fieldname=''):
        """
        return True if content uses CKeditor
        """
        context = aq_inner(self.context)
        request = self.request
        if self. _memberUsesCKeditor() or self._isAnonymous():
            if not fieldname:
                return True
            if not hasattr(context, 'getField'):
                return True
            field = context.getField(fieldname)
            if not field:
                return True
            text_format = request.get('%s_text_format' %
                                      fieldname,
                                      context.getContentType(fieldname))
            content = field.getEditAccessor(context)()
            try:
                if content.startswith('<!--'):
                    return False
            except:
                return False
            return 'html' in text_format.lower()
        return False
