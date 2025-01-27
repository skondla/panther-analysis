from panther_base_helpers import aws_rule_context, deep_get


def rule(event):
    if (
        event.get("eventSource", "") == "iam.amazonaws.com"
        and event.get("eventName", "") == "UpdateLoginProfile"
    ):
        return (
            deep_get(event, "requestParameters", "userName")
            != deep_get(event, "userIdentity", "arn").split("/")[-1]
        )
    return False


def title(event):
    return (
        f"User [{deep_get(event, 'userIdentity', 'arn').split('/')[-1]}] "
        f"changed the password for "
        f"[{deep_get(event, 'requestParameters','userName')}]"
    )


def alert_context(event):
    return aws_rule_context(event)
