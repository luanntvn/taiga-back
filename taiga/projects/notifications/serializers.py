# Copyright (C) 2014-2015 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014-2015 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2015 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json

from taiga.base.api import serializers
from taiga.users.models import User

from . import models
from . import choices


class NotifyPolicySerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField("get_project_name")

    class Meta:
        model = models.NotifyPolicy
        fields = ('id', 'project', 'project_name', 'notify_level')

    def get_project_name(self, obj):
        return obj.project.name


class WatcherSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'full_name')
