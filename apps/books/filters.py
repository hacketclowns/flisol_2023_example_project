from django_filters import rest_framework as djfilters


class BookFilterSet(djfilters.FilterSet, djfilters.BaseInFilter):
    family_friendly = djfilters.BooleanFilter(method="family_friendly_filter")

    def family_friendly_filter(self, queryset, name, value):
        print(name)
        print(value)
        if value:
            return queryset.family_friendly()
        else:
            return queryset
