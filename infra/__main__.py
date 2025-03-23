"""A Google Cloud Python Pulumi program"""

import os

import pulumi
import pulumi_gcp as gcp

ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
# create bucket resource for ammo listings
bucket = gcp.storage.Bucket(
    "ammoseekr-ammo-listings", location="US", public_access_prevention="enforced"
)
# Export the DNS name of the bucket
pulumi.export("ammo_listings", bucket.url)

# create our service account
service_account = gcp.serviceaccount.Account(
    "execution_account",
    account_id="execution-account",
    display_name="Service Account for application execution",
)
pulumi.export("service_acct_email", service_account.email)

# give the service account + admin account access to the bucket
members = [service_account.email.apply(lambda val: f"serviceAccount:{val}")]
if ADMIN_EMAIL:
    members.append(f"user:{ADMIN_EMAIL}")
admin = gcp.organizations.get_iam_policy(
    bindings=[
        {
            # TODO: separate service account into storage user and admin into storage admin
            "role": "roles/storage.admin",
            "members": members,
        },
    ]
)
policy = gcp.storage.BucketIAMPolicy(
    "policy", bucket=bucket.name, policy_data=admin.policy_data
)
