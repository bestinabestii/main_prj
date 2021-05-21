from django.contrib import admin

# Register your models here.
from.models import user_login
from.models import state_master
from.models import district_master
from.models import collectorate_user
from.models import official_user
from.models import user_details
from.models import disaster_report
from.models import disaster_followup
from.models import disaster_followup_allocation
from.models import disaster_master
from.models import general_info
from.models import disaster_pic
from.models import district_news
from.models import volunteer_details
from.models import volunteer_job_allocation
from.models import volunteer_followup
from.models import user_chat

admin.site.register(user_login)
admin.site.register(state_master)
admin.site.register(district_master)
admin.site.register(collectorate_user)
admin.site.register(official_user)
admin.site.register(user_details)
admin.site.register(disaster_report)
admin.site.register(disaster_followup)
admin.site.register(disaster_followup_allocation)
admin.site.register(disaster_master)
admin.site.register(general_info)
admin.site.register(disaster_pic)
admin.site.register(district_news)
admin.site.register(volunteer_details)
admin.site.register(volunteer_job_allocation)
admin.site.register(volunteer_followup)
admin.site.register(user_chat)


