.. _pattern_extraction_procedures:

*****************************
Pattern Extraction Procedures
*****************************

Before learning about specific patterns it makes sense to learn about how to
extract patterns because "(w)riting patterns in your own field can change the
way you think about that field(.)" and "(i)t can make you a better
practititioner." (Bergin 2013, pos. 74)

Following the basic, high abstraction procedure:

* Identify the potential subject matter (Bergin 2013, pos. 107).

 * a: What structure needs to be created?
 * b: What problem need to be solved?
   E.g. problems during adding features to an existing software project
   occured. You want to build a better software design. Your subject is
   design patterns.
 * c: If you do not have ideas about a and b you (i) do not have enough
   expertise or (ii) you do not have access to it. If (i) is true take your
   time and try it again. If (ii) collect data beeing able to describe the
   best known solution related to the pattern.

* Identify the format of the pattern description dependent on the subject
  matter (Bergin 2013, pos. 119).

 * a: Represent explicit meta-data as sections.
   E.g. name, context, problem, solution, implementation examples, etc. are
   common in technical subject matters.
 * a: Represent implicit meta-data as hints within sections.
   E.g. hints can crosslink different patterns even over subject matter
   boundaries which arehard to document in a structural manner. Think of
   object-oriented principles as patterns and a concret "implementation" with a
   design pattern.
 * b: Represent implicit meta-data typologically and structure the text
   regarding the explicit meata-data.
   E.g. The text is structured as paragraphs according to the explicit
   meta-data. Bold or italic text formatting makes implicit meta-data
   "visible".
 * Define the sequencial structure how the meta-data is arranged. The relation
   between the meta-data should be as obvious as possible. E.g. the forces 
   should follow the problem (Bergin 2013, pos. 185).

* Optional, when pattern in relation to a pattern language: Identify the
  format of the pattern language. "The pattern language is (at
  least) a collection of patterns that work together and admit "sequences" of
  patterns that solve problems larger than those of the individual
  patterns." (Bergin 2013, pos. 133)

 * Identify the forces which shall be resolved.
 * Priorice the forces which shall be resolved.
 * Identify patterns which address the problem to be solved considering the
   prioriticed forces. Begin with "large scale" patterns, end with
   "small scale" patterns. The resulting context after appliying a pattern has
   to fit the context before applying the next pattern.
 * Choose a representation which eases to get the "big picture". The "big
   picture" can be communicated much easier with graphics.

* Identify the content of the meta-data.

 * Identify the context. The context has to be about the situation "when" you
   consider using this pattern (Bergin 2013, pos. 164).
 * Identify the problem. The problem has to require action to be answered,
   should be recurring and should be expressed in a single sentence.
   Explanatory material should be avoided. Prefer a "stating" over "asking"
   formulation.
 * Identify forces. Think about "why" this solution is choosen. The solution
   should balance all forces which "(...) push in all directions and with
   different
   levels of intensity (...)" (Bergin 2013, pos. 208). Forces are important
   because it helps you to choose between different patterns, pattern
   variantions, implementation alternatives, etc. addressing the same context
   and overall resulting context related to the problem but with different
   weighting and consideration of the single forces. With forces the solution
   may be validated. E.g. quality attributes like scalability, complexity,
   maintainability, testability, etc. are forces which have to be balanced by
   a design pattern.
 * Identify a solution or solution alternatives. The "what" should be
   formulated as a single sentence.

* Iterate over the extraction process. An example of this iterative process
  with different pattern versions and a discussion about each can be found in
  (Bergin 2013, pos. 410). More examples can be found (Bergin 2013, pos. 667).
