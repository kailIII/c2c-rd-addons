# -*- coding: utf-8 -*-
{
     "name"         : "Budget Create",
     "version"      : "1.0",
     "author"       : "Camptocamp Austria",
     "website"      : "http://www.chricar.at/ChriCar",
     "description"  : """
     Create budget lines derived from account_move_lines of previous periods.
     this is helpful for planning fixed costs and often a good starting point 
     for variable costs and revenues.
     the budget items can, but must not be identical to accounts.
     On demand missing budget items are created with the same structure than accounts
     Usually the budget must be created before the year ends. Therefore the source 
     periods may overlap (Example use month Oct 2010 to Sept 2011 as basis for 2012)

     """,
     "category"     : "Accounting & Finance",
     "depends"      : ["c2c_budget"],
     "init_xml"     : [],
     "demo_xml"     : [],
     "update_xml"   : ["budget_view.xml"],
     "active"       : False,
     "installable"  : True,
}
