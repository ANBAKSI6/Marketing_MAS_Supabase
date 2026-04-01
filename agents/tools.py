from .ad_copy_agent import create_ad_copy
from .domain_agent import get_domain_suggestions
from .email_campaign_agent import create_email_campaign
from .logo_agent import generate_logo
from .seo_agent import generate_seo_keywords
from .social_media_agent import create_social_media_content
from .strategy_agent import create_marketing_strategy
from .tagline_agent import generate_taglines

tools = [
    create_ad_copy,
    get_domain_suggestions,
    create_email_campaign,
    generate_logo,
    generate_seo_keywords,
    create_social_media_content,
    create_marketing_strategy,
    generate_taglines,
]