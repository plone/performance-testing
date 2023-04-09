This repository is archived and read only.

If you want to unarchive it, then post to the [Admin & Infrastructure (AI) Team category on the Plone Community Forum](https://community.plone.org/c/aiteam/55).

==============================================================================
Plone Performance Testing
==============================================================================

Run buildout::

  $ python bootstrap-buildout.py
  $ bin/buildout

Start Instance::

  $ bin/instance start

Run jMeter Test::

  $ jmeter -n -t PloneTestplan.jmx

Miscellaneous
-------------

Performance Sprints:

  * http://plone.org/events/sprints/past-sprints/copenhagen-performance-sprint
  * http://www.coactivate.org/projects/plone-performance-sprint-2008/
  * http://ploneconf2009.org/program/sprint/plone-4-performance-sprint

Old Resources:

  * https://svn.plone.org/svn/collective/JMeterTestPlans/trunk/
