from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48,null=False)
    account = models.CharField(max_length=48,unique=True,null=False)
    passwd = models.CharField(max_length=128,null=False)
    status = models.IntegerField(null=False,default=0)  # 0:在用，1:停用
    role = models.IntegerField(null=False,default=0)  #0:普通用户；1：中心审批人员、2：运维经理、3：运维人员、10,：超级管理员

    def __repr__(self):
        return '{}_{}'.format(self.id,self.name)
    __str__ = __repr__