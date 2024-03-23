symptom('Headache').
symptom('Forgetting').
symptom('Nausea').
symptom('Dizziness').
symptom('Fatigue').
symptom('Blurredvision').
symptom('Moodswing').

treatment('Headache', 'Rest, hydration, over-the-counter pain relievers.').
treatment('Forgetting', 'Cognitive exercises, healthy diet, stress management.').
treatment('Nausea', 'Anti-nausea medications, hydration, small, bland meals.').
treatment('Dizziness', 'Rest, hydration, addressing underlying causes like low blood sugar or inner ear issues.').
treatment('Fatigue', 'Adequate sleep, balanced diet, regular exercise.').
treatment('Blurredvision', 'Corrective lenses, eye exercises, addressing underlying eye conditions.').
treatment('Moodswing', 'Counseling, therapy, lifestyle changes, medication if necessary.').

:- dynamic patient/2.
input :-
    repeat,
    symptom(X),
    write('Does the patient have '),
    write(X),
    write('? '),
    read(Y),
    assert(patient(X,Y)),
    output.

disease(stress_related_cognitive_impairment):-
	patient('Headache', yes),
    patient('Forgetting', yes).

disease(migraines):-
    not(disease(stress_Related_cognitive_impairment)),
	patient('Nausea', yes),
    patient('Forgetting', yes),
    patient('Dizziness', yes).

disease(vestibular_disorder):-
    not(disease(stress_Related_cognitive_impairment)),
    not(disease(migraines)),
	patient('Dizziness', yes),
    patient('Blurredvision', yes).

disease(depression):-
    not(disease(stress_Related_cognitive_impairment)),
    not(disease(migraines)),
    not(disease(vestibular_disorder)),
	patient('Fatigue', yes),
    patient('Moodswing', yes).

disease(dementia):-
    not(disease(stress_Related_cognitive_impairment)),
    not(disease(migraines)),
    not(disease(vestibular_disorder)),
    not(disease(depression)),
	patient('Forgetting', yes),
    patient('Moodswing', yes).

disease(low_sugar):-
    not(disease(stress_Related_cognitive_impairment)),
    not(disease(migraines)),
    not(disease(vestibular_disorder)),
    not(disease(depression)),
    not(disease(dementia)),
	patient('Dizziness', yes),
    patient('Blurredvision', yes),
	patient('Nausea', yes).

output:-
    nl,
    possible_diseases,
    nl,
    advice.

possible_diseases :- disease(X), write('The patient may suffer from '), write(X), nl.
advice :- symptom(X), patient(X, yes), treatment(X,Y), write(Y), nl.
