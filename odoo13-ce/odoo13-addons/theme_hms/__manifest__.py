# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management System',
    'version' : '1.0',
    'summary' : 'Hospital Management Software',
    'category': 'Productivity',
    'sequence': -100,
    'description': """
    Make the lock date irreversible:

    * You cannot define stricter conditions on advisors than on users. Then, the lock date on advisor must be set before the lock date for users.
    * You cannot lock a period that is not finished yet. Then, the lock date for advisors must be set before the last day of the previous month.
    * The new lock date for advisors must be set after the previous lock date.
    """,
    'license': 'LGPL-3',
    'application' : True,
    'installable' : True,
    'depends' : [],
    'data': [],
}
