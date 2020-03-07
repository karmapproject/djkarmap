from django.test import TestCase
from django.contrib.auth.models import User

from .models import *

class JobGroupTest(TestCase):

    def setUp(self):
        JobGroup.objects.create(title='just a test of JobGroup model')


    def test_job_group_title(self):
        job_group = JobGroup.objects.get(id=1)
        expected_object_name =f'{job_group.title}'
        self.assertEqual(expected_object_name, 'just a test of JobGroup model')


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