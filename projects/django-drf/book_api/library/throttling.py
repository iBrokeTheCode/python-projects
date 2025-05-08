from rest_framework.throttling import AnonRateThrottle


class CustomRateThrottle(AnonRateThrottle):
    scope = "custom"
