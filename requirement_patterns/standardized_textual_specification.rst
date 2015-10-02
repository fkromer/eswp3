.. _standardized_textual_specification:

******************************************
Standardized Textual Specification Pattern
******************************************

:Context:
 The **only** test case related to a textual documented requirement failed but
 it is not possible to identify the root cause.

:Problem:
 The requirement is not "traceable" because it includes several other
 requirements implicitly.

:Solution:
 Indentify the included atomic requirements. You must be able to formulate every
 requirement with a standardized textual description. Change the existing test
 case and add new test cases for the new requirements.

:Resulting context:
 The existing requirement and the new ones are traceable.
