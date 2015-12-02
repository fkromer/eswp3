.. state_transition_testing:

************************
State Transition Testing
************************

High level pattern for systematic derivation of test cases for state based
behavior (unit/component/system).

:Context:
 A function or a collection of functions which has not been generated
 automatically with a model-driven approach (assuming a high code generation
 quality STT would not detect any faults) has state-based behavior. The
 behavior is represented as table, activity chart or state chart in the test
 basis.

:Problem:
 19 faults categories exist in the context of state based behavior in total.
 15 of them may be detected with state transition testing when designed with
 care. The remaining (Broekman and Notenboom 2003, section "11.2.1 Fault
 Categories") It is not obvious how to derivate test cases to detect for 

:Solution:
 - compose the state-event table
 - compose the transition tree
 - compose test script legal test cases
 - compose test script illegal test cases
 - compose the test script guards
 
:Model example:
 Test cases for the state chart of a video cassette recorder are derived (Broekman and Notenboom 2003, section "11.2.2.2 Composing the state-event table").

:Resulting Context:
 15 of the 19 fault categories related to state-based behavior can be
 detected (state without incoming transition, missing inital state, additional
 state, missing state, 
 ). Applying STT leads to a high test effort. In the **model example** above
 from 5 states with 18 state transitions 62 test cases in 14 test paths are
 derived. Apply **statistical usage testing** to detect
 faults of category "incorrect implementation of guard". Apply **error guessing** to detect faults of category "reaction takes place to an undefined event (trap door)".
