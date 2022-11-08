from hstrat import hstrat

stratum_retention_policy = hstrat.geom_seq_nth_root_tapered_algo.Policy(
    parameterizer=hstrat.PropertyAtMostParameterizer(
        target_value=127,
        policy_evaluator=hstrat.MrcaUncertaintyAbsExactEvaluator(
            at_num_strata_deposited=256,
            at_rank=0,
        ),
        param_lower_bound=1,
        param_upper_bound=1024,
    ),
)

individual1 = hstrat.HereditaryStratigraphicColumn(
    stratum_retention_policy=stratum_retention_policy,
)
individual2 = hstrat.HereditaryStratigraphicColumn(
    stratum_retention_policy=stratum_retention_policy,
)

individual1_child1 = individual1.CloneDescendant()

hstrat.does_have_any_common_ancestor(individual1, individual2)  # -> False
hstrat.does_have_any_common_ancestor(
    individual1_child1, individual2)  # -> False

individual1_grandchild1 = individual1_child1.CloneDescendant()
individual1_grandchild2 = individual1_child1.CloneDescendant()

result = hstrat.calc_rank_of_mrca_bounds_between(
    individual1_grandchild1,
    individual1_grandchild2,
)  # -> (1, 2)

print(result)
