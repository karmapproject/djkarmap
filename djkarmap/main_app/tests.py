from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point

from .models import *


class JobGroupTest(TestCase):

    def setUp(self):
        JobGroup.objects.create(title='just a test of JobGroup model')

    def test_job_group_title(self):
        job_group = JobGroup.objects.get(id=1)
        expected_object_name = f'{job_group.title}'
        self.assertEqual(expected_object_name, 'just a test of JobGroup model')


class JobTest(TestCase):

    def setUp(self):
        title = 'just a test of Jub model'
        location = Point(51, 35)
        group = JobGroup.objects.create(title='just a test of JobGroup model')
        job_type = 1
        description = "just a description for Job model"

        Job.objects.create(title=title, location=location,
                           group=group, job_type=job_type, description=description)

    def test_job_title(self):
        job_title = Job.objects.get(id=1)
        expected_object_name = f'{job_title}'
        self.assertEqual(expected_object_name, 'just a test of Jub model')


class SkillTest(TestCase):

    def setUp(self):
        title = 'just a test of Skil model'
        description = 'just a description test of Skil model'

        Skil.objects.create(title=title, description=description)

    def test_skill_title(self):
        skill_title = Skil.objects.get(id=1)
        expected_object_name = f'{skill_title}'
        self.assertEqual(expected_object_name, 'just a test of Skil model')


# TODO solve errors main_app.models.Skil.DoesNotExist: Skil matching query does not exist.
# class  EmploeeTest(TestCase):

#     def setUp(self):
#         user = User.objects.create_user(username='test_user')

#         skill_1 = Skil.objects.create(title='st1', description='sd1')
#         skill_2 = Skil.objects.create(title='st2', description='sd2')


#         job_title1, job_title2 = 'jt1', 'jt2'
#         location1, location2 = Point(51.1, 35.1), Point(51.2, 35.2)
#         group1, group2 = JobGroup.objects.create(title='gt1'), JobGroup.objects.create(title='gt2')
#         job_type1, job_type2 = 1, 2
#         description1, description2 = "des1", "des2"

#         job1 = Job.objects.create(title=job_title1, location=location1, group=group1, job_type=job_type1, description=description1)
#         job2 = Job.objects.create(title=job_title2, location=location2, group=group2, job_type=job_type2, description=description2)

#         emploee = Employee.objects.create(user=user)
#         emploee.save()

#         emploee.searchfor.add(skill_1, skill_2)
#         emploee.searchfor.add(job1, job2)


#     def test_emploee_test(self):
#         employee_username = Employee.objects.get(id=1)
#         expected_object_name = f'{employee_username}'
#         self.assertEqual(expected_object_name, 'test_user')


# class  EmploerTest(TestCase):

#     def setUp(self):
#         pass

#     def test_emploer_test(self):
#         pass


# class  EmploerTest(TestCase):

#     def setUp(self):
#         pass

#     def test_emploer_test(self):
#         pass


# # TODO CHECK error in this test
# class JobOrderTest(TestCase):

#     def setUp(self):
#         user = User.objects.all().first()
#         job1 = Job.objects.all().first()
#         job2 = Job.objects.all().last()
#         job_order = JobOrder(user=user)
#         job_order.searchfor.add(job1, job2)
#         job_order.save()


#     def test_job_order_content(self):
#         job_order = JobOrder.objects.get(id=1)
#         expected_object_name = f'{job_order.user.usernam}'
#         self.assertEqual(expected_object_name, 'jus test for JobOrder model')
