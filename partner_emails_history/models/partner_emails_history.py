# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Saritha Sahadevan(<https://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models


class PartnerEmailHistory(models.Model):
    _inherit = 'res.partner'

    def sent_email_history(self):
        action = self.env.ref('mail.action_view_mail_mail')
        result = action.read()[0]
        result['domain'] = [('email_from', '=', self.email)]
        return result

    def received_email_history(self):
        action = self.env.ref('mail.action_view_mail_mail')
        result = action.read()[0]
        result['domain'] = ['|', ('email_to', '=', self.email), ('recipient_ids', '=', self.email)]
        return result
