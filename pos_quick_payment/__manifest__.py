# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Aswani PC(<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': "Pos Quick Payment",
    'version': '10.0.1.0.0',
    'summary': """Quick Payment Buttons In POS""",
    'description': """
        This module add extra quick payment buttons in pos payment screen.
    """,
    'author': "Cybrosys Techno Solutions",
    'maintainer': 'Cybrosys Techno Solutions',
    'company': "Cybrosys Techno Solutions",
    'website': "https://www.cybrosys.com",
    'category': 'Point Of Sale',
    'depends': ['point_of_sale'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'qweb': ['static/src/xml/pos_quick_payment.xml'],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
