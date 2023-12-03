from django.db import models


# Create your models here.
class DepositProducts(models.Model):
    dcls_month = models.TextField()
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    mtrt_int = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    max_limit = models.IntegerField(null=True)


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()




class SavingProducts(models.Model):
    dcls_month = models.TextField()
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    mtrt_int = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    max_limit = models.IntegerField(null=True)


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100) #저축 금리 유형명 (단리, 복리)
    rsrv_type_nm = models.TextField()                    #적립 유형명 (자유적립식 등등)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()                     # 최고 우대 금리
    save_trm = models.IntegerField()

















# class SubscribedProduct(models.Model):
#     # 가입한 유저
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # 종류(적금인지 예금인지)
#     type = models.TextField(null=True)
#     # 금융상품코드
#     fin_prdt_cd = models.TextField(null=True)
#     # 금융회사명
#     kor_co_nm = models.TextField(null=True)
#     # 금융상품명
#     fin_prdt_nm = models.TextField(null=True)
#     # 최고한도
#     max_limit = models.IntegerField(null=True)
#     # 가입액
#     amount = models.IntegerField()
#     #공시 종료일
#     dcls_end_day = models.TextField(null=True)
#     # 적립유형
#     rsrv_type = models.TextField(null=True)
#     # 적립유형명
#     rsrv_type_nm = models.TextField(null=True)
#     # 저축금리유형
#     intr_rate_type = models.TextField(null=True)
#     # 저축금리유형명
#     intr_rate_type_nm = models.TextField(null=True)
#     # 저축기간(개월)
#     save_trm = models.IntegerField(null=True)
#     # 저축금리
#     intr_rate = models.FloatField(null=True)
#     # 최고우대금리
#     intr_rate2 = models.FloatField(null=True)






# class SubscribedSaving(models.Model):
#         # 가입한 유저
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # 금융상품코드
#     fin_prdt_cd = models.TextField(null=True)
#     # 금융회사명
#     kor_co_nm = models.TextField(null=True)
#     # 금융상품명
#     fin_prdt_nm = models.TextField(null=True)
#     # 최고한도
#     max_limit = models.IntegerField(null=True)
#     # 가입액
#     saving_amount = models.IntegerField()
#     #공시 종료일
#     dcls_end_day = models.TextField(null=True)
#     # 적립유형
#     rsrv_type = models.TextField(null=True)
#     # 적립유형명
#     rsrv_type_nm = models.TextField(null=True)
#     # 저축금리유형
#     intr_rate_type = models.TextField(null=True)
#     # 저축금리유형명
#     intr_rate_type_nm = models.TextField(null=True)
#     # 저축기간(개월)
#     save_trm = models.IntegerField(null=True)
#     # 저축금리
#     intr_rate = models.FloatField(null=True)
#     # 최고우대금리
#     intr_rate2 = models.FloatField(null=True)