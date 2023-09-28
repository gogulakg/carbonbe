from django.db import models
from uuid import uuid4
# Create your models here.

class CarbonTable(models.Model):
    material_specification = models.CharField(max_length=100,blank=False,null=True)
    a1_a3=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    a4=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    wf=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    c2=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    c3_c4=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    c2_c4=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    d=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    total_a1_a5=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    total_a_c=models.DecimalField( max_digits=20, decimal_places=3,blank=False,null=True)
    a1=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    a2=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    a3=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    a5=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    b1=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    b2=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    b3=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    b4=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    b5=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    c1=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    c3=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    c4=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000',null=True)
    tenant_id=models.IntegerField(null=True,default='0001')
    class Meta:

        db_table = 'carbon_table'
    
    def __str__(self):
        return self.material_specification

class StructuralElement(models.Model):
    element_name=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = 'structural_element'

    def __str__(self):
        return self.element_name


class ElementGroup(models.Model):
    group_name=models.CharField(max_length=100,blank=False)
    
    class Meta:
        db_table = 'element_group'
    
    def __str__(self):
        return self.group_name








class Carbon(models.Model):
    
    carbon_table=models.ForeignKey(CarbonTable,null=True,related_name="carbon",on_delete=models.CASCADE)
    substructural_element=models.ForeignKey(StructuralElement,null=True,on_delete=models.CASCADE)
    element_group=models.ForeignKey(ElementGroup,null=True,on_delete=models.CASCADE)
    gia=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    

    class Meta:
        db_table = 'carbon'
    
    @property
    def A1_A3(self):
        return (self.carbon_table.a1_a3)*(self.quantity)
    

    @property
    def A4(self):
        return (self.carbon_table.a4)*(self.quantity)
    

    @property
    def A5w(self):
        return (self.carbon_table.wf)*(self.quantity)
    

    @property
    def C2(self):
        return (self.carbon_table.c2)*(self.quantity)
    
    @property
    def C3_C4(self):
        return (self.carbon_table.c3_c4)*(self.quantity)
    

    @property
    def C2_C4(self):
        return (self.carbon_table.c2_c4)*(self.quantity)
    

    @property
    def D(self):
        return (self.carbon_table.d)*(self.quantity)
    

    @property
    def TOTAL_A1_A5(self):
        return (self.carbon_table.total_a1_a5)*(self.quantity)
    

    @property
    def TOTAL_A_C(self):
        return (self.carbon_table.total_a_c)*(self.quantity)

    @property
    def A_C_m2(self):
        return ((self.carbon_table.total_a_c)*(self.quantity)*(1000))/self.gia
    
    @property
    def A1_A5_m2(self):
        return ((self.carbon_table.total_a1_a5)*(self.quantity)*(1000))/self.gia


#############################################################

# a1_a3=models.IntegerField(null=True)
    # a4=models.IntegerField(null=True)
    # wf=models.IntegerField(null=True)
    # c2=models.IntegerField(null=True)
    # c3_c4=models.IntegerField(null=True)
    # c2_c4=models.IntegerField(null=True)
    # d=models.IntegerField(null=True)
    # total_a1_a5=models.IntegerField(null=True)
    # total_a_c=models.IntegerField(null=True)
    # a1=models.IntegerField(null=True,default='0.000')
    # a2=models.IntegerField(null=True,default='0.000')
    # a3=models.IntegerField(null=True,default='0.000')
    # a5=models.IntegerField(null=True,default='0.000')
    # b1=models.IntegerField(null=True,default='0.000')
    # b2=models.IntegerField(null=True,default='0.000')
    # b3=models.IntegerField(null=True,default='0.000')
    # b4=models.IntegerField(null=True,default='0.000')
    # b5=models.IntegerField(null=True,default='0.000')
    # c1=models.IntegerField(null=True,default='0.000')
    # c3=models.IntegerField(null=True,default='0.000')
    # c4=models.IntegerField(null=True,default='0.000')






# class CarbonReference(models.Model):
#     material_specification = models.CharField(max_length=100,blank=False)
#     a1_a3=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     a4=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     wf=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     c2=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     c3_c4=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     c2_c4=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     d=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     total_a1_a5=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     total_a_c=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     a1=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     a2=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     a3=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     a5=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     b1=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     b2=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     b3=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     b4=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     b5=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     c1=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     c3=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
#     c4=models.DecimalField( max_digits=20, decimal_places=3,blank=True,default='0.000')
    
#     reference_id= models.CharField(max_length=18, default=f, unique=True)
#     class Meta:

#         db_table = 'carbon_reference'
    
#     def __str__(self):
#         return self.material_specification

    
 # func1=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
    # def aa3(self):
    #     return ''.join((self.carbon_table.a1_a3)*(self.quantity))
    
# carbon_table=models.ForeignKey(CarbonTable,related_name='carbon_table')

#################################################################










###################################################################

# class InputTable(models.Model):
#     carbon_table=models.ForeignKey(CarbonReference,null=True,on_delete=models.CASCADE)
#     substructural_element=models.ForeignKey(StructuralElement,null=True,on_delete=models.CASCADE)
#     element_group=models.ForeignKey(ElementGroup,null=True,on_delete=models.CASCADE)
#     gia=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     quantity=models.DecimalField( max_digits=20, decimal_places=3,blank=False)

#     class Meta:
#         db_table = 'input_table'
 





# class Singer(models.Model):
#     name=models.CharField(max_length=100)
#     gender=models.CharField(max_length=100)
#     # song=models.ForeignKey(Song, on_delete=models.CASCADE,related_name='singer')
#     def __str__(self):
#         return self.name


# class Song(models.Model):
#     title=models.CharField(max_length=100)
#     singer=models.ForeignKey(Singer, on_delete=models.CASCADE,related_name='song')
#     duration=models.IntegerField()
#     def __str__(self):
#         return self.title




# class Category(models.Model):
#     name = models.CharField(max_length=100,null=True)

#     def __unicode__(self):
#         return self.name


# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE,null=True)

#     def __unicode__(self):
#         return self.name















# class CarbonTable2(models.Model):
#     # carbon_table=models.ForeignKey(CarbonTable,related_name='carbon_table')
#     substructural_element=models.ForeignKey(StructuralElement,null=True,on_delete=models.CASCADE)
#     element_group=models.ForeignKey(ElementGroup,null=True,on_delete=models.CASCADE)
#     gia=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     quantity=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     material_specification = models.CharField(max_length=100,blank=False)
#     a1_a3=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     a4=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     wf=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     c2=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     c3_c4=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     c2_c4=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     d=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     total_a1_a5=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     total_a_c=models.DecimalField( max_digits=20, decimal_places=3,blank=False)
#     class Meta:

#         db_table = 'carbon_table2'
    
#     def __str__(self):
#         return self.material_specification

