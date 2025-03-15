from asyncio import Future
import datetime
from http import client
from typing import dataclass_transform

from django.db.models.base import resolve_relation
from django.db.models.query_utils import select_related_descend
from django.http import response
from django.template import context
from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone
from django.utils.translation.trans_real import reset_cache
from django.views.generic import detail

from .models import Question

# Create your tests here.


def create_question(question_text, days):
    """
    Create a question with the given 'question_text' and published
    the
    given number of 'days' offset to now (nwgative for questions
    in the past, positive for questions that have yet to be
    published).
    """

    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """
        if no questions exist, an appropiate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains((response, "No polls are available. "))

        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        # Questions with a pud_date in the past are displayed on the index page.

        question = create_question(question_text="past question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(response.context["latest_question_list"], [question])

    def test_future_question(self):
        """
        questions with a pub_date hin the future aren't displayed on
        the index
        """
        create_question(question_text="future_question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")

        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_quesion(self):
        """
        Even if both past and future questions exist, only past
        questions are displayed.
        """
        question = create_question(question_text="Past question.", days=30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may didplay multiple questions.
        """

        quesston1 = create_question(question_text="Past question1", days=30)
        question2 = create_question(question_text="Past question2", days=5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [quesston1, question2],
        )


class QuestionDetailViewTest(TestCase):
    def test_future_questio(self):
        """
        The detail view of a question with a pub_date in the Future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future quesston.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past question.", days=5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionModelTests(TestCase):
    def test_was_published_recntly_with_old_question(self):
        """
        was_published_recently() returns False for questions whose
        pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recntly_with_recent_question(self):
        """
        was_published_recently() returns False for questions whose
        pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

