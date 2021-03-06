# -*- coding: utf-8 -*-

Pm = {
    "P1_interval": {
        "id": "Pm_P1_interval",
        "label": "\mathsf{P}_{\mathsf{1}}",
        "dimension": 2,
        "image": "P1_interval.png",
        "weight_functions": "\dof{2}{0}{0}{0}{1} = 2",
        "exterior_calc": "\Pm{1}{0}{1}",
        "code": '("P", interval, 1)',
        "code_alt": '("P-", interval, 1, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_interval": {
        "id": "Pm_P2_interval",
        "label": "\mathsf{P}_{\mathsf{2}}",
        "dimension": 3,
        "image": "P2_interval.png",
        "weight_functions": "\dof{2}{1}{0}{0}{1} \pl \dof{1}{0}{1}{1}{1} = 3",
        "exterior_calc": "\Pm{2}{0}{1}",
        "code": '("P", interval, 2)',
        "code_alt": '("P-", interval, 2, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_interval": {
        "id": "Pm_P3_interval",
        "label": "\mathsf{P}_{\mathsf{3}}",
        "dimension": 4,
        "image": "P3_interval.png",
        "weight_functions": "\dof{2}{2}{0}{0}{1} \pl \dof{1}{1}{1}{1}{2} = 4",
        "exterior_calc": "\Pm{3}{0}{1}",
        "code": '("P", interval, 3)',
        "code_alt": '("P-", interval, 3, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "dP0_interval": {
        "id": "Pm_dP0_interval",
        "label": "\mathsf{dP}_{\mathsf{0}}",
        "dimension": 1,
        "image": "dP0_interval.png",
        "weight_functions": "\dof{1}{0}{0}{1}{1} = 1",
        "exterior_calc": "\Pm{1}{1}{1}",
        "code": '("DP", interval, 0)',
        "code_alt": '("P-", interval, 1, 1)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP1_interval": {
        "id": "Pm_dP1_interval",
        "label": "\mathsf{dP}_{\mathsf{1}}",
        "dimension": 2,
        "image": "dP1_interval.png",
        "weight_functions": "\dof{1}{1}{0}{1}{2} = 2",
        "exterior_calc": "\Pm{2}{1}{1}",
        "code": '("DP", interval, 1)',
        "code_alt": '("P-", interval, 2, 1)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_interval": {
        "id": "Pm_dP2_interval",
        "label": "\mathsf{dP}_{\mathsf{2}}",
        "dimension": 3,
        "image": "dP2_interval.png",
        "weight_functions": "\dof{1}{2}{0}{1}{3} = 3",
        "exterior_calc": "\Pm{3}{1}{1}",
        "code": '("DP", interval, 2)',
        "code_alt": '("P-", interval, 3, 1)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "P1_triangle": {
        "id": "Pm_P1_triangle",
        "label": "\mathsf{P}_{\mathsf{1}}",
        "dimension": 3,
        "image": "P1_triangle.png",
        "weight_functions": "\dof{3}{0}{0}{0}{1} = 3",
        "exterior_calc": "\Pm{1}{0}{2}",
        "code": '("P", triangle, 1)',
        "code_alt": '("P-", triangle, 1, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_triangle": {
        "id": "Pm_P2_triangle",
        "label": "\mathsf{P}_{\mathsf{2}}",
        "dimension": 6,
        "image": "P2_triangle.png",
        "weight_functions": "\dof{3}{1}{0}{0}{1} \pl \dof{3}{0}{1}{1}{1} = 6",
        "exterior_calc": "\Pm{2}{0}{2}",
        "code": '("P", triangle, 2)',
        "code_alt": '("P-", triangle, 2, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_triangle": {
        "id": "Pm_P3_triangle",
        "label": "\mathsf{P}_{\mathsf{3}}",
        "dimension": 10,
        "image": "P3_triangle.png",
        "weight_functions": "\dof{3}{2}{0}{0}{1} \pl \dof{3}{1}{1}{1}{2} \pl \dof{1}{0}{2}{2}{1} = 10",
        "exterior_calc": "\Pm{3}{0}{2}",
        "code": '("P", triangle, 3)',
        "code_alt": '("P-", triangle, 3, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "RT1_triangle": {
        "id": "Pm_RT1_triangle",
        "label": "\mathsf{RT}^{\mathsf{[e/f]}}_{\mathsf{1}}",
        "dimension": 3,
        "image": "RT1_triangle.png",
        "weight_functions": "\dof{3}{0}{0}{1}{1} = 3",
        "exterior_calc": "\Pm{1}{1}{2}",
        "code": '("RT[E,F]", triangle, 1)',
        "code_alt": '("P-", triangle, 1, 1)',
        "color": "orange",
        "citation": "Raviart and Thomas, Lecture Notes in Math. 606 (1977)"
    },
    "RT2_triangle": {
        "id": "Pm_RT2_triangle",
        "label": "\mathsf{RT}^{\mathsf{[e/f]}}_{\mathsf{2}}",
        "dimension": 8,
        "image": "RT2_triangle.png",
        "weight_functions": "\dof{3}{1}{0}{1}{2} \pl \dof{1}{0}{1}{2}{2} = 8",
        "exterior_calc": "\Pm{2}{1}{2}",
        "code": '("RT[E,F]", triangle, 2)',
        "code_alt": '("P-", triangle, 2, 1)',
        "color": "orange",
        "citation": "Raviart and Thomas, Lecture Notes in Math. 606 (1977)"
    },
    "RT3_triangle": {
        "id": "Pm_RT3_triangle",
        "label": "\mathsf{RT}^{\mathsf{[e/f]}}_{\mathsf{3}}",
        "dimension": 15,
        "image": "RT3_triangle.png",
        "weight_functions": "\dof{3}{2}{0}{1}{3} \pl \dof{1}{1}{1}{2}{6} = 15",
        "exterior_calc": "\Pm{3}{1}{2}",
        "code": '("RT[E,F]", triangle, 3)',
        "code_alt": '("P-", triangle, 3, 1)',
        "color": "orange",
        "citation": "Raviart and Thomas, Lecture Notes in Math. 606 (1977)"
    },
    "dP0_triangle": {
        "id": "Pm_dP0_triangle",
        "label": "\mathsf{dP}_{\mathsf{0}}",
        "dimension": 1,
        "image": "dP0_triangle.png",
        "weight_functions": "\dof{1}{0}{0}{2}{1} = 1",
        "exterior_calc": "\Pm{1}{2}{2}",
        "code": '("DP", triangle, 0)',
        "code_alt": '("P-", triangle, 1, 2)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP1_triangle": {
        "id": "Pm_dP1_triangle",
        "label": "\mathsf{dP}_{\mathsf{1}}",
        "dimension": 3,
        "image": "dP1_triangle.png",
        "weight_functions": "\dof{1}{1}{0}{2}{3} = 3",
        "exterior_calc": "\Pm{2}{2}{2}",
        "code": '("DP", triangle, 1)',
        "code_alt": '("P-", triangle, 2, 2)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_triangle": {
        "id": "Pm_dP2_triangle",
        "label": "\mathsf{dP}_{\mathsf{2}}",
        "dimension": 6,
        "image": "dP2_triangle.png",
        "weight_functions": "\dof{1}{2}{0}{2}{6} = 6",
        "exterior_calc": "\Pm{3}{2}{2}",
        "code": '("DP", triangle, 2)',
        "code_alt": '("P-", triangle, 3, 2)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "P1_tetrahedron": {
        "id": "Pm_P1_tetrahedron",
        "label": "\mathsf{P}_{\mathsf{1}}",
        "dimension": 4,
        "image": "P1_tetrahedron.png",
        "weight_functions": "\dof{4}{0}{0}{0}{1} = 4",
        "exterior_calc": "\Pm{1}{0}{3}",
        "code": '("P", tetrahedron, 1)',
        "code_alt": '("P-", tetrahedron, 1, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_tetrahedron": {
        "id": "Pm_P2_tetrahedron",
        "label": "\mathsf{P}_{\mathsf{2}}",
        "dimension": 10,
        "image": "P2_tetrahedron.png",
        "weight_functions": "\dof{4}{1}{0}{0}{1} \pl \dof{6}{0}{1}{1}{1} = 10",
        "exterior_calc": "\Pm{2}{0}{3}",
        "code": '("P", tetrahedron, 2)',
        "code_alt": '("P-", tetrahedron, 2, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_tetrahedron": {
        "id": "Pm_P3_tetrahedron",
        "label": "\mathsf{P}_{\mathsf{3}}",
        "dimension": 20,
        "image": "P3_tetrahedron.png",
        "weight_functions": "\dof{4}{2}{0}{0}{1} \pl \dof{6}{1}{1}{1}{2} \pl \dof{4}{0}{2}{2}{1} = 20",
        "exterior_calc": "\Pm{3}{0}{3}",
        "code": '("P", tetrahedron, 3)',
        "code_alt": '("P-", tetrahedron, 3, 0)',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "N1e1_tetrahedron": {
        "id": "Pm_N1e1_tetrahedron",
        "label": "\mathsf{N1}^{\mathsf{e}}_{\mathsf{1}}",
        "dimension": 6,
        "image": "N1e1_tetrahedron.png",
        "weight_functions": "\dof{6}{0}{0}{1}{1} = 6",
        "exterior_calc": "\Pm{1}{1}{3}",
        "code": '("N1E", tetrahedron, 1)',
        "code_alt": '("P-", tetrahedron, 1, 1)',
        "color": "red",
        "citation": u"Nédélec, Numer. Math. 35 (1980)"
    },
    "N1e2_tetrahedron": {
        "id": "Pm_N1e2_tetrahedron",
        "label": "\mathsf{N1}^{\mathsf{e}}_{\mathsf{2}}",
        "dimension": 20,
        "image": "N1e2_tetrahedron.png",
        "weight_functions": "\dof{6}{1}{0}{1}{2} \pl \dof{4}{0}{1}{2}{2} = 20",
        "exterior_calc": "\Pm{2}{1}{3}",
        "code": '("N1E", tetrahedron, 2)',
        "code_alt": '("P-", tetrahedron, 2, 1)',
        "color": "red",
        "citation": u"Nédélec, Numer. Math. 35 (1980)"
    },
    "N1e3_tetrahedron": {
        "id": "Pm_N1e3_tetrahedron",
        "label": "\mathsf{N1}^{\mathsf{e}}_{\mathsf{3}}",
        "dimension": 45,
        "image": "N1e3_tetrahedron.png",
        "weight_functions": "\dof{6}{2}{0}{1}{3} \pl \dof{4}{1}{1}{2}{6} \pl \dof{1}{0}{2}{3}{3} = 45",
        "exterior_calc": "\Pm{3}{1}{3}",
        "code": '("N1E", tetrahedron, 3)',
        "code_alt": '("P-", tetrahedron, 3, 1)',
        "color": "red",
        "citation": u"Nédélec, Numer. Math. 35 (1980)"
    },
    "N1f1_tetrahedron": {
        "id": "Pm_N1f1_tetrahedron",
        "label": "\mathsf{N1}^{\mathsf{f}}_{\mathsf{1}}",
        "dimension": 4,
        "image": "N1f1_tetrahedron.png",
        "weight_functions": "\dof{4}{0}{0}{2}{1} = 4",
        "exterior_calc": "\Pm{1}{2}{3}",
        "code": '("N1F", tetrahedron, 1)',
        "code_alt": '("P-", tetrahedron, 1, 2)',
        "color": "yellow",
        "citation": u"Nédélec, Numer. Math. 35 (1980)"
    },
    "N1f2_tetrahedron": {
        "id": "Pm_N1f2_tetrahedron",
        "label": "\mathsf{N1}^{\mathsf{f}}_{\mathsf{2}}",
        "dimension": 15,
        "image": "N1f2_tetrahedron.png",
        "weight_functions": "\dof{4}{1}{0}{2}{3} \pl \dof{1}{0}{1}{3}{3} = 15",
        "exterior_calc": "\Pm{2}{2}{3}",
        "code": '("N1F", tetrahedron, 2)',
        "code_alt": '("P-", tetrahedron, 2, 2)',
        "color": "yellow",
        "citation": u"Nédélec, Numer. Math. 35 (1980)"
    },
    "N1f3_tetrahedron": {
        "id": "Pm_N1f3_tetrahedron",
        "label": "\mathsf{N1}^{\mathsf{f}}_{\mathsf{3}}",
        "dimension": 36,
        "image": "N1f3_tetrahedron.png",
        "weight_functions": "\dof{4}{2}{0}{2}{6} \pl \dof{1}{1}{1}{3}{12} = 36",
        "exterior_calc": "\Pm{3}{2}{3}",
        "code": '("N1F", tetrahedron, 3)',
        "code_alt": '("P-", tetrahedron, 3, 2)',
        "color": "yellow",
        "citation": u"Nédélec, Numer. Math. 35 (1980)"
    },
    "dP0_tetrahedron": {
        "id": "Pm_dP0_tetrahedron",
        "label": "\mathsf{dP}_{\mathsf{0}}",
        "dimension": 1,
        "image": "dP0_tetrahedron.png",
        "weight_functions": "\dof{1}{0}{0}{3}{1} = 1",
        "exterior_calc": "\Pm{1}{3}{3}",
        "code": '("DP", tetrahedron, 0)',
        "code_alt": '("P-", tetrahedron, 1, 3)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP1_tetrahedron": {
        "id": "Pm_dP1_tetrahedron",
        "label": "\mathsf{dP}_{\mathsf{1}}",
        "dimension": 4,
        "image": "dP1_tetrahedron.png",
        "weight_functions": "\dof{1}{1}{0}{3}{4} = 4",
        "exterior_calc": "\Pm{2}{3}{3}",
        "code": '("DP", tetrahedron, 1)',
        "code_alt": '("P-", tetrahedron, 2, 3)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_tetrahedron": {
        "id": "Pm_dP2_tetrahedron",
        "label": "\mathsf{dP}_{\mathsf{2}}",
        "dimension": 10,
        "image": "dP2_tetrahedron.png",
        "weight_functions": "\dof{1}{2}{0}{3}{10} = 10",
        "exterior_calc": "\Pm{3}{3}{3}",
        "code": '("DP", tetrahedron, 2)',
        "code_alt": '("P-", tetrahedron, 3, 3)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    }
}
