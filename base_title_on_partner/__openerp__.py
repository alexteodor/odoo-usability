# -*- encoding: utf-8 -*-
##############################################################################
#
#    Base Title on Partner module for OpenERP
#    Copyright (C) 2014 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Title on Partner',
    'version': '0.1',
    'category': 'Partner',
    'license': 'AGPL-3',
    'summary': 'Display title on all the form views of partners',
    'description': """
Title on Partner
================

By default, OpenERP doesn't display the title field on all the partner form views. This module fixes it.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['base'],
    'data': ['partner_view.xml'],
    'installable': True,
    'active': False,
}
