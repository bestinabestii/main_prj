from django.db import models

# Create your models here.
# user_login - id int ,uname varchar,password varchar,u_type varchar


class user_login(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=25)

# state_master - id int,state_name varchar


class state_master(models.Model):
    id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100)

# district_master - id,district,state_master_id


class district_master(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.CharField(max_length=50)
    state_master_id = models.IntegerField()

# collectorate_user - id,user_id,name,addr1,addr2,addr3,pin,district_id


class collectorate_user(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    addr1 = models.CharField(max_length=150)
    addr2 = models.CharField(max_length=150)
    addr3 = models.CharField(max_length=150)
    pin = models.IntegerField()
    district_id = models.IntegerField()

# official_user - id,user_id,name,name_details,role,contact,email,district_id


class official_user(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    name_details = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    district_id = models.IntegerField()

# user_details - id,user_id,fname,lname,gender,dob,addr1,addr2,addr3,pin,district_id,id_name,id_no,dt,tm,status,
# email,contact


class user_details(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    addr = models.CharField(max_length=150)
    pin = models.IntegerField()
# district_id = models.IntegerField()
#id_name = models.CharField(max_length=50)
# id_no = models.IntegerField()
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)

# disaster_report - id,user_id,disaster_master_id,addr,description,location_info,dt,tm,status


class disaster_report(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    disaster_master_id = models.IntegerField()
    addr = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    location_info = models.CharField(max_length=150)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

# disaster_followup - id,disaster_report_id,remark,dt,tm,status


class disaster_followup(models.Model):
    id = models.AutoField(primary_key=True)
    disaster_report_id = models.IntegerField()
    remark = models.CharField(max_length=100)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

# disaster_followup_allocation - id,disaster_report_id,user_id,dt,tm,status


class disaster_followup_allocation(models.Model):
    id = models.AutoField(primary_key=True)
    disaster_report_id = models.IntegerField()
    user_id = models.IntegerField()
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

# disaster_master - id,disaster_name,disaster_descp


class disaster_master(models.Model):
    id = models.AutoField(primary_key=True)
    disaster_name = models.CharField(max_length=50)
    disaster_descp = models.CharField(max_length=50)

# general_info -id,description,g_type,path


class general_info(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150)
    g_type = models.CharField(max_length=50)
    path = models.CharField(max_length=50)

# disaster_pic - id,disaster_report_id,pic_path,dt,tm


class disaster_pic(models.Model):
    id = models.AutoField(primary_key=True)
    disaster_report_id = models.IntegerField()
    pic_path = models.CharField(max_length=50)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)

# district_news - id,district_id,subject,news,dt,tm,status


class district_news(models.Model):
    id = models.AutoField(primary_key=True)
    district_id = models.IntegerField()
    subject = models.CharField(max_length=100)
    news = models.CharField(max_length=200)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

# volunteer_details - id,user_id,fname,lname,gender,dob,addr1,addr2,addr3,pin,district_id,id_name,id_no,dt,tm,status,email,contact


class volunteer_details(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    addr = models.CharField(max_length=150)
    pin = models.IntegerField()
#district_id = models.IntegerField()
#id_name = models.CharField(max_length=50)
#id_no = models.IntegerField()
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)



# volunteer_job_allocation - id,user_id,job_description,contact_name,contact_number,addr,dt,tm,status


class volunteer_job_allocation(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    job_description = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    addr = models.CharField(max_length=150)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)


# volunteer_followup - id,job_id,remark,dt,tm,status


class volunteer_followup(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.IntegerField()
    remark = models.CharField(max_length=100)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

# user_chat - id,from_user_id,to_user_id,msg,dt,tm,status


class user_chat(models.Model):
    id = models.AutoField(primary_key=True)
    from_user_id = models.IntegerField()
    to_user_id = models.IntegerField()
    msg = models.CharField(max_length=100)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=50)




