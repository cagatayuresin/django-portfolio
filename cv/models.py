# -*- coding: utf-8 -*-
from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(
        verbose_name="Skill Name",
        max_length=20,
    )

    class Level(models.IntegerChoices):
        NONE = 0, "None"
        BEGINNER = 1, "Beginner"
        MEDIUM = 2, "Medium"
        ADVANCED = 3, "Advanced"
        EXPERT = 4, "Expert"
        MASTER = 5, "Master"

    id = models.AutoField(primary_key=True)
    level = models.IntegerField(
        choices=Level.choices,
        default=Level.NONE,
        verbose_name="Level",
    )
    icon = models.ImageField(
        verbose_name="Skill Icon",
    )

    def __str__(self):
        return f"{self.skill_name} | {self.level * '★' + (5 - self.level) * '☆'}"


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(
        verbose_name="Project Name",
        max_length=200,
    )
    years = models.CharField(verbose_name="Years", max_length=20, null=True, blank=True)
    description = models.CharField(
        verbose_name="Project Description",
        max_length=300,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Project: {self.years} | {self.project_name}"


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.CharField(
        verbose_name="School Name",
        max_length=100,
    )
    department = models.CharField(
        verbose_name="University Department",
        max_length=50,
    )
    years = models.CharField(verbose_name="Years", max_length=20, null=True, blank=True)
    projects = models.ManyToManyField(
        Project,
        verbose_name="Projects",
        related_name="education_projects",
    )

    def __str__(self):
        return f"Education: {self.school} | {self.department}"


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    employer = models.CharField(
        verbose_name="Employer",
        max_length=100,
        null=False,
        blank=False,
    )
    occupation = models.CharField(
        verbose_name="Occupation",
        max_length=50,
        null=False,
        blank=False,
    )
    years = models.CharField(verbose_name="Years", max_length=20, null=True, blank=True)
    description = models.CharField(
        verbose_name="Project Description",
        max_length=300,
        null=True,
        blank=True,
    )
    projects = models.ManyToManyField(
        Project, verbose_name="Projects", related_name="experience_projects", blank=True
    )

    def __str__(self):
        return f"Experience: {self.employer} | {self.occupation}"


class CV(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.ImageField(
        verbose_name="Skill Icon",
    )
    name_surname = models.CharField(verbose_name="Name of the Person", max_length=50)
    occupation = models.CharField(verbose_name="Job", max_length=50)
    email = models.EmailField(
        verbose_name="Contact Email", null=True, blank=True, max_length=50
    )
    cv = models.TextField(verbose_name="The CV of The Person")
    skills = models.ManyToManyField(
        Skill,
        verbose_name="Skills",
        related_name="cv_skills",
    )
    experiences = models.ManyToManyField(
        Experience,
        verbose_name="Experiences",
        related_name="cv_experiences",
    )
    educations = models.ManyToManyField(
        Education,
        verbose_name="Educations",
        related_name="cv_educations",
    )
    languages = models.ManyToManyField(
        Skill,
        verbose_name="Languages",
        related_name="cv_languages",
    )

    def __str__(self):
        return f"CV | {self.name_surname}"
