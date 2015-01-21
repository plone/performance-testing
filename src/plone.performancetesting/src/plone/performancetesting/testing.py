from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class PloneperformancetestingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.performancetesting
        xmlconfig.file(
            'configure.zcml',
            plone.performancetesting,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.performancetesting:default')
        portal = getSite()
        wf_tool = getToolByName(portal, "portal_workflow")
        wf_tool.setDefaultChain("simple_publication_workflow")


PLONE_PERFORMANCETESTING_FIXTURE = PloneperformancetestingLayer()
PLONE_PERFORMANCETESTING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_PERFORMANCETESTING_FIXTURE,),
    name="PloneperformancetestingLayer:Integration"
)
PLONE_PERFORMANCETESTING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_PERFORMANCETESTING_FIXTURE, z2.ZSERVER_FIXTURE),
    name="PloneperformancetestingLayer:Functional"
)
