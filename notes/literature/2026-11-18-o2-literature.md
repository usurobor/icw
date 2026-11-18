# O2 literature: identity of moving patterns (18 Nov)

Search for prior work on the open problem of O2: a criterion, computed from the
rule and the actual history, that says when a pattern-tracing in a
deterministic local automaton is one persisting individual. Sources already
run or listed in the repo (Israeli and Goldenfeld, Shalizi et al., Dennett,
Krakauer et al., Beer et al. 2024, Montévil and Mossio, Salmon's mark
criterion) appear only where something new was found.

Each entry gives a citation, a summary in my words, and a verdict for the
three failure groups of 17 Nov and for symmetry:

- *B*: bundles (union of distant gliders, glider plus far spark, gun with its
  emitted gliders, fed eaters as one).
- *P*: ending into a product (a glider continued into collision debris or into
  the eater's merged piece).
- *N*: ending into nothing (annihilation).
- *S*: symmetry (a map that preserves the rule preserves the verdict).

Verdicts: *definition* (offers a definition we can run), *diagnostic* (tells us
why something fails or where to look), *irrelevant*. Items marked "read" were
read in the primary text or its arXiv version; "abstract" means only the
abstract or a secondary record was reached.

## Information dynamics

**L-1. Lizier, Prokopenko and Zomaya: local information dynamics.** Read.
Lizier, J. T., Prokopenko, M. and Zomaya, A. Y. (2008). "Local information
transfer as a spatiotemporal filter for complex systems." *Physical Review E*
77: 026110. (2010). "Information modification and particle collisions in
distributed computation." *Chaos* 20: 037109. (2012). "Local measures of
information storage in complex distributed computation." *Information
Sciences* 208: 39–54. Lizier, J. T. and Prokopenko, M. (2010).
"Differentiating information transfer and causal effect." *European Physical
Journal B* 73: 605–615.

Local transfer entropy, active information storage and separable information
are computed at each space-time point from an ensemble of observed runs, with
the destination's past of length k as context. In elementary automata gliders
light up as transfer along their direction of motion, domains as storage, and
collisions as points of negative separable information (modification). The
2010 EPJ B paper adds a sharp result: the interventional measure (Ay and
Polani's information flow) does not single out gliders; it sees the domain as
equally causal. Gliders appear only in the predictive, ensemble-relative
measure that conditions on the destination's own past.

- B: irrelevant. Point measures do not group cells.
- P: diagnostic. Separable information locates the contact event in space
  and time. That gives the vertex where a glider continuity should end; it
  gives no continuity.
- N: diagnostic, same as P.
- S: diagnostic. Invariant only if the ensemble is invariant under the map.
- For ICW: explains C11 and C12. A per-cell interventional measure sees cells;
  the glider-shaped signal comes from conditioning on a past, which brings an
  ensemble back in.

**L-2. Partial information decomposition filters.** Abstract only. Flecker,
B., Alford, W., Beggs, J. M., Williams, P. L. and Beer, R. D. (2011). "Partial
information decomposition as a spatiotemporal filter." *Chaos* 21: 037104.
Lizier, J. T., Flecker, B. and Williams, P. L. (2013). "Towards a
synergy-based approach to measuring information modification." IEEE
Symposium on Artificial Life; arXiv:1303.3440.

Synergy (information two sources give only jointly) is proposed as the proper
measure of modification, replacing the heuristic separable information. Same
role as L-1 for ICW.

- B, N, S: irrelevant. P: diagnostic (marks collisions as synergy).

**L-3. Krakauer et al., with Bertschinger et al. and Bourrat.** Read.
Krakauer et al. (2020) is in the repo. Bertschinger, N., Olbrich, E., Ay, N.
and Jost, J. (2006). "Information and closure in systems theory." In *Explorations in
the Complexity of Possible Life* (GWAL 7), 9–19. IOS Press. Bourrat, P.
(2024). "Adding causality to the information-theoretic perspective on
individuality." *European Journal for Philosophy of Science* 14: 9.

The formal core of Krakauer et al. is three quantities over a fixed system S
and environment E: autonomy A* = I(S'; S), conditional autonomy
A = I(S'; S | E), and environmental leak nC = I(S'; E | S); informational
closure (Bertschinger et al.) is nC = 0. Bourrat shows A* can be high when the
environment is a common cause of S at both times, and proposes an
interventional version, I(S'; do(S)). Neither paper handles a moving S.

- B: diagnostic. All three quantities are additive over independent
  subsystems, so a union of two individuals scores as the sum and passes. This
  is what C11 found.
- P, N: irrelevant.
- S: diagnostic, as L-1.
- For ICW: Bourrat supports the repo's knockout (interventional) choice.

**L-4. Causal emergence and Ψ.** Read (Rosas). Hoel, E. P., Albantakis, L.
and Tononi, G. (2013). "Quantifying causal emergence shows that macro can beat
micro." *PNAS* 110: 19790–19795. Rosas, F. E., Mediano, P. A. M., Jensen, H.
J., Seth, A. K., Barrett, A. B., Carhart-Harris, R. L. and Bor, D. (2020).
"Reconciling emergences." *PLoS Computational Biology* 16: e1008289.

Hoel scores a fixed coarse-graining by effective information under maximal
interventions. Rosas et al. score a macro feature V by Ψ, its self-prediction
minus the summed prediction from single cells. In the Game of Life they take V
as the vector "a particle of type j is on the board", found by pattern
matching, and get Ψ ≈ 0.58 > 0.

- B: diagnostic. V ignores which particle is which, so it groups every glider
  into one variable. Positive Ψ says a glider-level variable predicts itself;
  it says nothing about which glider.
- P, N, S: irrelevant.

## Integration and causation over a trajectory

**L-5. Biehl: ι-entities (complete local integration).** Read (thesis,
chapters 1–6 partly). Biehl, M., Ikegami, T. and Polani, D. (2016). "Towards
information based spatiotemporal patterns as a foundation for agent
representation in dynamical systems." *Proc. ALIFE 2016*, 722–729;
arXiv:1605.05676. Biehl, M., Ikegami, T. and Polani, D. (2017). "Specific and
complete local integration of patterns in Bayesian networks." *Entropy* 19:
230. Biehl, M. (2017). *Formal approaches to a definition of agents.* PhD
thesis, University of Hertfordshire; arXiv:1704.02716.

A spatiotemporal pattern is a set of cell-time-value assignments, possibly
spread over many steps, evaluated on one trajectory. Its specific local
integration for a partition is log p(pattern) minus the sum of log p(block)
over the partition's blocks. Complete local integration is the minimum over
all partitions; an ι-entity is a pattern with a positive minimum. For a
pattern whose blocks are independent the value is exactly 0, so it is refused.
The thesis names "half a glider together with half a block far away" as the
kind of grouping the measure is built to refuse. The ι-entities may
interpenetrate (no exclusion), the measure needs a distribution over initial
conditions, and the cost is a Bell number of partitions times the full joint
distribution: the author estimates petabytes for a 7 × 7 Game of Life over
three steps. No glider was computed.

- B: definition, with a limit. Out-of-reach bundles and splices get exactly 0
  by independence, which is reach again. Bundles within reach (bi-block, fed
  eaters) share inputs, so their blocks are correlated under the ensemble and
  can score positive. C16 met the same failure.
- P: diagnostic. Without exclusion, glider-plus-debris and
  glider-plus-block-plus-debris can both be entities. An exclusion clause
  (L-7) would pick one.
- N: irrelevant; untested.
- S: definition. The thesis proves the measure is invariant under
  automorphisms that preserve the distribution (section 4.5). Rule 184's
  car-hole map preserves the uniform measure, so the verdicts match.
- For ICW: the only general definition found of entities as whole space-time
  patterns with a clause aimed at bundles. Whole-trajectory, so it has no
  per-step flicker.

**L-6. Albantakis et al.: actual causation.** Read. Albantakis, L., Marshall,
W., Hoel, E. and Tononi, G. (2019). "What caused what? A quantitative account
of actual causation using dynamical causal networks." *Entropy* 21: 459.

For one actual transition, every subset of the present (an occurrence) gets
one actual cause: the subset of the past that specifies it with the most
irreducible information α. Irreducible means α > 0 under its minimum
information partition; ties go to the smaller subset. Probabilities come from
the transition rule by causal marginalization (unconstrained inputs set
uniformly), so no observed ensemble is needed. High-order causes are allowed:
in an AND gate the pair is the single cause of the output. The paper treats
one step and notes that k steps work the same way.

- B: definition. Two non-interacting parts give α = 0 for the partition that
  separates them, so their union has no joint cause. This holds within reach
  as long as neither part changes the other's next state on the actual
  transition, which covers the bi-block where ensemble measures fail.
- P: definition. The debris occurrence's actual cause is glider and block
  together, irreducibly; the glider's stage alone is not its cause, so a
  glider chain ends at contact while a chain for the interaction continues.
  This matches the owner's rulings.
- N: definition, with a caveat. The dead cells after an annihilation are
  caused by the pair jointly. Absences as causes are delicate in threshold
  rules and need a check.
- S: definition. Uniform marginalization is invariant under any state
  permutation that preserves the rule.
- For ICW: closest to C10 plus C13 in spirit, with two things the repo has not
  run: irreducibility over partitions on the actual transition, and an
  exclusion clause. Per step, so the interaction flicker of C9 returns unless
  the k-step form is used over the interaction interval.

**L-7. Integrated information Φ.** Read (2015, partly). Albantakis, L. and
Tononi, G. (2015). "The intrinsic cause-effect power of discrete dynamical
systems: from elementary cellular automata to adapting animats." *Entropy*
17: 5472–5502. Albantakis, L. et al. (2023). "Integrated information theory
(IIT) 4.0." *PLoS Computational Biology* 19: e1011465 (not read).

Φ is computed for fixed sets of units. Complexes are non-overlapping sets that
are local maxima of Φ; reducible rules (0, 51, 204) have Φ = 0. Nothing is
said about gliders: the units are cells, so a complex is a set of sites.

- B: diagnostic. Irreducibility refuses unions of non-interacting sets, for
  fixed sets only.
- P: diagnostic. The exclusion postulate (maximal, non-overlapping) is the
  clause L-5 lacks.
- N: irrelevant. S: as L-6.

## Computational mechanics and particles

**L-8. Domain-particle decomposition and particle catalogues.** Read
(Hordijk). Hanson and Crutchfield (1997) are in the repo. Hordijk, W.,
Crutchfield, J. P. and Mitchell, M. (1998). "Mechanisms of emergent
computation in cellular automata." *Parallel Problem Solving from Nature V*,
LNCS 1498, 613–622.

Regular domains are filtered out; particles are the boundaries left, each with
a period, displacement and velocity. Interactions are catalogued as reactions
(α + β → γ, decay α → γ + β, annihilation μ + β → ∅). Colliding particles are
replaced at once by the products. A ballistic particle model built from the
catalogue predicts the automaton's computation closely.

- B: definition. Each particle is one boundary trace; a union is never an
  entry.
- P: definition, by convention. Identity ends at every interaction; products
  are new. This is the owner's ruling for gliders. The eater's persistence has
  no place: a participant that survives needs an added rule (L-12).
- N: definition. Annihilation is a catalogued event.
- S: definition. Domains are defined by space-time symmetry, independent of
  symbol names, so a map that preserves the rule maps domains to domains and
  particles to particles.
- For ICW: in the Game of Life the domain is the quiescent background, so the
  filter is "anything alive". The decomposition helps once domains are
  nontrivial, as in rule 184.

**L-9. Local causal states.** Read (partly). Rupe, A. and Crutchfield, J. P.
(2018). "Local causal states and discrete coherent structures." *Chaos* 28:
075312.

Past light cones are grouped by the distribution they give over future light
cones. Domains are regions where the causal-state field is invariant under
space-time translations; coherent structures are localized breaks of that
symmetry. A filter with a principled basis; no identity over time.

- B, P, N: irrelevant. S: diagnostic, as L-8. C2 ran depth 1; depth 2 is the
  real test.

**L-10. Pivato: defects and their invariants; rule 184 as ballistic
annihilation.** Read (2005 arXiv; 2007 abstract). Pivato, M. (2007). "Defect
particle kinematics in one-dimensional cellular automata." *Theoretical
Computer Science* 377: 205–228; arXiv:math/0506417. Pivato, M. (2007).
"Algebraic invariants for crystallographic defects in cellular automata."
*Ergodic Theory and Dynamical Systems* 27: 199–240. Krug, J. and Spohn, H.
(1988). *Physical Review A* 38: 4271. Belitsky, V. and Ferrari, P. A. (1995).
*Journal of Statistical Physics* 80: 517 (both via secondary record).

A defect is a region where a configuration fails to belong to an invariant
subshift. A defect that survives iteration and stays bounded is a particle.
Removable defects can be erased by a finite change; essential ones cannot.
Algebraic invariants (cocycles, homology and homotopy of the subshift) explain
why defects persist and constrain collision outcomes. In rule 184 at density
1/2, the background is 1010…; a pair 00 moves right, a pair 11 moves left, and
they annihilate on contact. The map that swaps 0 and 1 and reflects space
preserves the rule and swaps the two defect types.

- B: diagnostic.
- P: definition in rule 184. A defect's charge (excess cars) is conserved; in
  a merger of jams the merged jam carries both charges. The invariant does not
  pick a survivor, so the owner's "larger continues" is a further rule.
- N: definition in rule 184. Annihilation of opposite charges is predicted.
- S: definition. Defect-based support is equivariant by construction: a jam
  and its hole image get one verdict. This is the fix the owner's symmetry
  ruling asks of C15's element clause.
- For ICW: in the Game of Life every finite pattern is a removable defect of
  the empty background, so the invariants are trivial there.

**L-11. Solitons in integrable automata.** Read (Ferrari and Gabrielli).
Takahashi, D. and Satsuma, J. (1990). "A soliton cellular automaton."
*Journal of the Physical Society of Japan* 59: 3514–3519. Ferrari, P. A. and
Gabrielli, D. (2020). "Box-ball system: soliton and tree decomposition of
excursions." arXiv:1906.06405. Nishinari, K. and Takahashi, D. (1998).
"Analytical properties of ultradiscrete Burgers equation and rule-184
cellular automaton." *Journal of Physics A* 31: 5439–5450.

In the box-ball system, solitons are identified from a single configuration
by a pairing algorithm; the number of solitons of each size is conserved;
solitons of different sizes move at different speeds and pass through each
other. Identity through a collision is fixed by the conserved size. Ferrari
and Gabrielli also note that tagging one ball gives different motions under
different ball-moving rules that produce the same configuration map. Rule 184
is the ultradiscrete Burgers equation.

- B, N: irrelevant.
- P: diagnostic. A pattern can keep its identity through an interaction when
  a conserved quantity of the rule assigns it uniquely. The Game of Life has
  no such quantity, which supports "a glider ends at contact".
- S: diagnostic.
- For ICW: the tagged-ball remark matches the repo's audit that car identity
  needs an order-preserving convention beyond the rule.

## Philosophy of causal processes

**L-12. Beer's programme, with Gaul.** Read (2014 abstract and summaries; Gaul
2024, 2025). Beer, R. D. (2004). "Autopoiesis and cognition in the game of
life." *Artificial Life* 10: 309–326. (2014). "The cognitive domain of a
glider in the game of life." *Artificial Life* 20: 183–206. (2015).
"Characterizing autopoiesis in the game of life." *Artificial Life* 21: 1–19.
(2020). "An integrated perspective on the constitutive and interactive
dimensions of autonomy." *Proc. ALIFE 2020*, 202–209. Gaul, T. M. (2024).
"Autopoiesis in RealLife Euclidean automata." *Proc. ALIFE 2024*. Gaul, T. M.
(2025). *Biological organisation and viability.* Honors thesis, Indiana
University.

The glider's identity is its organization: a network of processes in which
each step's products enable the next. Its boundary is its live cells plus the
ring of dead cells in their neighbourhoods. In 2014, all 2²⁴ perturbations of
the surrounding ring are classified: a glider survives when the next state is
one of its 16 canonical configurations (any phase, orientation or chirality),
and otherwise falls into an absorbing "no glider" state. Gaul notes that an
organization read off observed sequences need not be unique, and leaves
collisions to future work.

- B: diagnostic. The boundary is drawn around one known glider; two are
  never considered.
- P: definition, type-relative. A participant continues through an
  interaction when its local state afterwards is again in its own viable set.
  The eater is restored and continues; the glider's output is no glider and it
  ends. This matches the owner's rulings, at the cost of a catalogue of each
  type's configurations.
- N: definition, same test.
- S: irrelevant. The boundary uses live cells.

**L-13. Salmon, Dowe and the gerrymander problem.** Read (SEP summary).
Dowe, P. (2000). *Physical Causation.* Cambridge University Press. Hitchcock,
C. (1995). "Salmon on explanatory relevance." *Philosophy of Science* 62:
304–320. Salmon, W. C. (1997). "Causality and explanation: a reply to two
critiques." *Philosophy of Science* 64: 461–477. Choi, S. (2002). "Causation
and gerrymandered world lines: a critique of Salmon." *Philosophy of Science*
69: 105–117. Dowe, P. (2007). "Causal processes." *Stanford Encyclopedia of
Philosophy*.

Dowe: a causal process is the world line of an object that possesses a
conserved quantity; an interaction is an intersection with exchange of one.
He admits "any old gerrymandered thing" as an object, except time-wise
gerrymanders. Hitchcock's shadow on a charged plate possesses charge at each
point; Dowe and Salmon reply that the shadowed plate segments form a time-wise
gerrymander. Choi shows the gerrymander problem returns at a charge-density
boundary.

- B: diagnostic. Spatial gerrymanders (bundles) are admitted by design.
- P: diagnostic. Exchange of a conserved quantity marks the interaction; it
  does not say who continues.
- N: irrelevant.
- S: diagnostic. In rule 184 cars and holes are both conserved, so the theory
  treats them alike. In the Game of Life nothing is conserved and every
  pattern is a pseudo-process.
- For ICW: the philosophy reached the same wall. Splices (time-wise
  gerrymanders) are refused only by presupposing an object's identity over
  time, and bundles pass.

**L-14. Genidentity.** Abstract only. Guay, A. and Pradeu, T. (2016). "To be
continued: the genidentity of physical and biological processes." In Guay and
Pradeu (eds.), *Individuals Across the Sciences*, 317–347. Oxford University
Press.

Identity through time as the continuous connection of the states a thing
passes through, with no permanent substrate; a "functional genidentity" for
biology; a process ontology.

- B, P, N, S: irrelevant for running; it names the relation O2 must define.

## Tracking in engineering and visualization

**L-15. Multi-object tracking.** Read (summaries). Reid, D. B. (1979). "An
algorithm for tracking multiple targets." *IEEE Transactions on Automatic
Control* 24: 843–854. Zhang, L., Li, Y. and Nevatia, R. (2008). "Global data
association for multi-object tracking using network flows." *CVPR 2008*.
Ristani, E. et al. (2016). "Performance measures and a data set for
multi-target, multi-camera tracking." *ECCV Workshops*, LNCS 9914, 17–35.

Tracks are paths through a graph of detections. Links are scored by a motion
model and appearance; entering and leaving cost a fixed amount; a global
optimization (multiple hypotheses, or a minimum-cost flow) gives each
detection to at most one track. A splice is an "identity switch", an error
measured against human annotation. Tracks are kept alive through occlusion
and merges.

- B: diagnostic. One detection per track refuses bundles by fiat; the
  detector defines the units.
- P: diagnostic. Trackers carry identity through merges, the opposite of the
  owner's ruling, because annotators do.
- N: diagnostic. A track ends after a set number of missed frames: a
  parameter.
- S: irrelevant.
- For ICW: a minimum-cost flow over the whole history, with link cost taken
  from the rule (C10's closeness), would assign identities globally and
  uniquely. The entry and exit costs are free parameters, as K was in C8.

**L-16. Feature tracking in scientific visualization.** Read (report and
summary). Samtaney, R., Silver, D., Zabusky, N. and Cao, J. (1994).
"Visualizing features and tracking their evolution." *IEEE Computer* 27:
20–27. Silver, D. and Wang, X. (1997). "Tracking and visualizing turbulent 3D
features." *IEEE Transactions on Visualization and Computer Graphics* 3:
129–141. Lukasczyk, J., Maciejewski, R., Weber, G. H., Garth, C. and Leitte,
H. (2017). "Nested tracking graphs." *Computer Graphics Forum* 36: 12–22.

Features are connected regions above a threshold. Features at successive
steps correspond by spatial overlap. Five events: continuation, creation,
dissipation, bifurcation, amalgamation. The result is a tracking graph.
Identity through an amalgamation is left unspecified. Lukasczyk et al. show the
graph changes with the threshold.

- B: definition. A feature is connected, so a distant union is never one.
- P: definition. Amalgamation is a vertex; a continuity is a run of
  one-to-one links between vertices.
- N: definition. Dissipation is a vertex.
- S: diagnostic. Threshold features privilege one state; use defect support
  (L-10).
- For ICW: the event list is the register's case list. Overlap and threshold
  are describer choices; in a cellular automaton the rule's neighbourhood and
  a knockout test can replace both.

**L-17. Topological tracking: Reeb graphs, the elder rule, vineyards.** Read
(abstracts). Edelsbrunner, H., Harer, J., Mascarenhas, A., Pascucci, V. and
Snoeyink, J. (2008). "Time-varying Reeb graphs for continuous space-time
data." *Computational Geometry* 41: 149–166. Edelsbrunner, H., Letscher, D.
and Zomorodian, A. (2002). "Topological persistence and simplification."
*Discrete and Computational Geometry* 28: 511–533. Cohen-Steiner, D.,
Edelsbrunner, H. and Morozov, D. (2006). "Vines and vineyards by updating
persistence in linear time." *Proc. SoCG 2006*, 119–126.

Contract each connected component of each time slice of the space-time
support to a point; the result is a Reeb graph whose edges are maximal runs of
one-to-one continuation and whose vertices are births, deaths, merges and
splits. In persistent homology the elder rule settles merges: the component
born earlier continues, the younger dies. Vineyards follow features
continuously through a changing function and list the points where they swap.

- B, P, N: definition. As L-16, with a graph that is canonical once support and
  adjacency are fixed.
- S: diagnostic, as L-16.
- For ICW: the owner's ruling that the larger jam continues is an elder rule
  with size in place of age. Both are canonical tie-breaks that make the
  graph assign one continuer; neither is read off the rule.

## Physics of excitations

**L-18. Quasiparticles and holes.** Read (secondary). Landau, L. D. (1956).
"The theory of a Fermi liquid." *Zh. Eksp. Teor. Fiz.* 30: 1058; *Sov. Phys.
JETP* 3: 920 (1957). Gelfert, A. (2003). "Manipulative success and the
unreal." *International Studies in the Philosophy of Science* 17: 245–263.

A quasiparticle is a collective excitation that behaves as a particle when its
decay rate is small next to its energy; its identity is graded by lifetime.
Particle-hole symmetry of the dynamics maps quasiparticles to quasiholes with
the same status. Gelfert discusses whether manipulable quasiparticles such as
holes count as real.

- B: irrelevant.
- P: diagnostic. Decay into products is graded by a rate. A glider in
  isolation is exact (no decay), so grading by lifetime says nothing until a
  collision.
- N: irrelevant.
- S: diagnostic. A direct precedent for the owner's ruling that a hole gets the
  verdict a car gets.

## What the sources say together

1. Bundles are refused in three ways. Connectivity of support (L-8, L-16,
   L-17) is reach plus a neighbourhood. One unit per track (L-15) is fiat.
   Irreducibility over partitions (L-5, L-6, L-7) gives an exact zero for
   independent parts. Computed over an ensemble (L-5) it fails for parts
   within reach that share inputs, as C16 failed. Computed on the actual
   transition with interventions (L-6) it can refuse the bi-block. The repo has
   not run the actual-transition form.
2. Every source with a rule for collisions ends identity at the interaction
   vertex, unless something assigns a continuer: a conserved quantity (L-10,
   L-11), restoration to the participant's own viable set (L-12), or a
   canonical tie-break (L-17). The owner's rulings coincide with this
   practice. Ending into a product is then a graph event to classify; no
   per-step flow measure is needed for it.
3. Symmetry passes by construction for definitions built from domain-relative
   defects (L-8, L-10) or from uniform interventional repertoires (L-6). It
   fails for definitions built on "live cells" in a rule with a 0/1 symmetry.
4. No source states the register's problem and solves it. Biehl (L-5) is the
   only general definition of entities as space-time patterns with a clause
   aimed at bundles; it is not computable at Game of Life scale and was never
   run on gliders. The domain-particle literature (L-8) and the tracking
   literature (L-16, L-17) get the owner's collision verdicts by convention.
   The philosophy (L-13) stalled where the register stalled: splices are
   refused by presupposing identity.

## Ranked formulations to try

**F-1. Event graph of the actual history.** Sources: L-8, L-10, L-12, L-16,
L-17. Support: the cells that differ from the rule's domain (in the Game of
Life, live cells; in rule 184, Pivato's defects, so the car-hole map sends
support to support). At each step, join support cells into pieces when
knocking one out changes the next state of the other's neighbourhood (C15's
contrast join). Link a piece at t to a piece at t+1 when knocking out the
first changes the second. Classify every vertex as continuation (1 to 1),
merge (k to 1), split (1 to k), birth or death; a branch that changes nothing
afterwards (idle exhaust) does not make a split. A carried pattern continuity
is a path of continuation links; it ends at a merge or a death. An
interaction whole is the subgraph from a merge to a split into pieces that
provably never link again. One crossing rule, declared once, decides who
continues through a merge: the unique closest continuer under C10's
closeness, which gives the larger jam in rule 184 and the restored eater
(L-12 test) in the Game of Life. Predictions: bundles and splices refused (no
path), endings into a product or nothing refused (vertex), symmetry by
construction. Cost: one knockout rerun per piece per step. Risk: the crossing
rule is where a patch could enter; it must be judged on unseen boards. Gain
over C15: the clauses become one graph with a fixed event list.

**F-2. Chained actual causation.** Source: L-6, with exclusion from L-7. For a
tracing with stages S_t, compute on each actual transition the actual cause
of S_{t+1} (its live and dead cells within the footprint) over candidate
purviews within reach, by α at the minimum information partition, with causal
marginalization uniform over unconstrained inputs. The tracing is carried
when, at every step, the actual cause of S_{t+1} is S_t (allowing idle
exhaust), the actual effect of S_t is S_{t+1}, and α > 0. To remove the
one-step flicker, run the same test on k-step transitions over the
interaction interval fixed before the run. Predictions: unions get α = 0;
debris has the glider-and-block pair as cause, so the glider ends at contact
and the pair's interaction whole holds; the eater's chain resumes after the
interval. Symmetry holds by construction. Cost: repertoires factor over
cells; the search over purviews is exponential, so restrict purviews to
F-1's pieces. Risks: dead cells as causes in a threshold rule; dependence on
the uniform marginalization.

**F-3. Complete local integration with exclusion, as a test of a family.**
Sources: L-5, L-7. For a tracing over a window of two or three steps, take its
cells and values as one space-time pattern. Compute its probability under
uniform random cells on its backward light cone (exact enumeration for small
cones, sampling otherwise). Score the bipartitions the register needs:
spatial halves, early against late, the tracing against the rest of its
interaction. Accept when the minimum is positive and no larger pattern in the
same history scores higher (exclusion). Prediction: out-of-reach bundles and
splices score exactly 0; the bi-block and fed eaters score positive and hold,
which would fail them. Value: if that prediction holds, the ensemble-
integration family (C11, C12, C16, L-3, L-5) is closed for bundles within
reach, and work moves to F-1 and F-2. Cost is high beyond three steps; run
it on the bi-block and the far-spark case first.

## Not yet read

IIT 4.0 (2023) in full; Pivato's 2007 invariants paper in full; Beer 2015 on
the glider's boundary in full; the Flecker et al. (2011) PID filter; Lizier's
2013 book, which may include the Game of Life.
