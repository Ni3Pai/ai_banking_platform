# ============================================
# AI Banking Platform — main.py
# ============================================

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from groq import Groq
import json
import os

# ============================================
# Setup
# ============================================
client_groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))
app = FastAPI(title="AI Banking Platform", version="1.0")

# ============================================
# AI Functions
# ============================================

def analyse_customer_structured(customer):
    response = client_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a banking risk analyst.
                Always respond with ONLY valid JSON, no other text.
                Use exactly this structure:
                {
                    "customer_name": "string",
                    "risk_score": number between 1-10,
                    "risk_level": "Low" or "Medium" or "High",
                    "reason": "one sentence explanation",
                    "recommendation": "one sentence action"
                }"""
            },
            {
                "role": "user",
                "content": f"""Analyse this customer:
                Name: {customer['name']}
                Balance: € {customer['balance']}
                Transactions: {customer['transactions']}
                Active: {customer['is_active']}"""
            }
        ]
    )
    return json.loads(response.choices[0].message.content)


def generate_user_story(requirement):
    response = client_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a senior AI Product Owner with
                10 years experience in banking and financial services.
                Respond with ONLY valid JSON in exactly this structure:
                {
                    "user_story": "As a [role] I want [feature] so that [benefit]",
                    "acceptance_criteria": ["Given...When...Then...", "Given...When...Then...", "Given...When...Then..."],
                    "definition_of_done": ["criterion 1", "criterion 2", "criterion 3"],
                    "story_points": number,
                    "priority": "High" or "Medium" or "Low"
                }"""
            },
            {
                "role": "user",
                "content": f"Generate a user story for this requirement: {requirement}"
            }
        ]
    )
    return json.loads(response.choices[0].message.content)


def check_eu_ai_act(use_case):
    response = client_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are an EU AI Act compliance expert specialising in financial services.
                Respond with ONLY valid JSON in exactly this structure:
                {
                    "use_case_summary": "brief summary",
                    "risk_tier": "Unacceptable" or "High Risk" or "Limited Risk" or "Minimal Risk",
                    "risk_tier_reason": "why this tier applies",
                    "compliance_requirements": ["req 1", "req 2", "req 3"],
                    "red_flags": ["flag 1", "flag 2"],
                    "recommended_actions": ["action 1", "action 2"],
                    "compliant_by": "date"
                }"""
            },
            {
                "role": "user",
                "content": f"Analyse this AI use case for EU AI Act compliance: {use_case}"
            }
        ]
    )
    return json.loads(response.choices[0].message.content)


def assess_taxonomy(client):
    if not client['nace_code']:
        return {
            "client_id": client['client_id'],
            "client_name": client['client_name'],
            "assessment_tier": "CANNOT ASSESS",
            "taxonomy_eligible": None,
            "taxonomy_aligned": None,
            "substantial_contribution": None,
            "dnsh_assessment": None,
            "minimum_safeguards": None,
            "revenue_kpi": None,
            "capex_kpi": None,
            "gaps": ["Insufficient data for any assessment"],
            "recommendations": ["Collect NACE code, sector and GHG data from client"]
        }

    capex_display = f"€ {client['capex_eur']:,}" if client['capex_eur'] else 'Not provided'

    context = f"""
    Client: {client['client_name']}
    Sector: {client['sector'] or 'Unknown'}
    NACE Code: {client['nace_code']}
    Main Purpose: {client['main_purpose'] or 'Not provided'}
    Sub Purpose: {client['sub_purpose'] or 'Not provided'}
    GHG Scope 1+2 (tonnes): {client['ghg_scope1_2_tonnes'] or 'Not provided'}
    Minimum Safeguards Compliant: {client['minimum_safeguards_compliant']}
    Annual Turnover: € {client['annual_turnover_eur']:,}
    CapEx: {capex_display}
    """

    if client['nace_code'] and client['main_purpose'] and client['sub_purpose'] and client['ghg_scope1_2_tonnes']:
        instruction = "Perform a complete 4-step EU Taxonomy assessment."
    elif client['nace_code'] and client['main_purpose']:
        instruction = "Perform a partial EU Taxonomy assessment."
    else:
        instruction = "Perform an eligibility check only based on NACE code."

    response = client_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a senior EU Taxonomy compliance expert at a Dutch bank.
                CRITICAL RULES:
                - Diesel or fossil fuel transport is NOT taxonomy aligned
                - Traditional blast furnace steel is NOT taxonomy aligned
                - Be conservative — when in doubt mark as not aligned
                Respond with ONLY valid JSON. No preamble, no markdown.
                {
                    "assessment_tier": "FULL" or "PARTIAL" or "ELIGIBILITY",
                    "taxonomy_eligible": true or false,
                    "taxonomy_aligned": true or false or null,
                    "substantial_contribution": {
                        "objective": "objective name",
                        "meets_criteria": true or false,
                        "reasoning": "one sentence"
                    },
                    "dnsh_assessment": {
                        "climate_mitigation": "Pass" or "Fail" or "Incomplete",
                        "climate_adaptation": "Pass" or "Fail" or "Incomplete",
                        "water": "Pass" or "Fail" or "Incomplete",
                        "circular_economy": "Pass" or "Fail" or "Incomplete",
                        "pollution": "Pass" or "Fail" or "Incomplete",
                        "biodiversity": "Pass" or "Fail" or "Incomplete",
                        "overall": "Pass" or "Fail" or "Incomplete"
                    },
                    "minimum_safeguards": "Pass" or "Fail" or "Incomplete",
                    "revenue_kpi": number or null,
                    "capex_kpi": number or null,
                    "gaps": ["gap 1"],
                    "recommendations": ["action 1"]
                }"""
            },
            {
                "role": "user",
                "content": f"{instruction}\n\nClient data:\n{context}"
            }
        ]
    )

    raw = response.choices[0].message.content
    try:
        clean = raw.strip()
        if clean.startswith("```"):
            clean = clean.split("```")[1]
            if clean.startswith("json"):
                clean = clean[4:]
        result = json.loads(clean.strip())
        result['client_id'] = client['client_id']
        result['client_name'] = client['client_name']
        return result
    except Exception as e:
        return {"error": str(e), "client_id": client['client_id']}


# ============================================
# API Endpoints
# ============================================

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Banking Platform",
        "version": "1.0",
        "tools": ["risk-assessment", "user-stories", "eu-ai-act", "eu-taxonomy"]
    }


class CustomerInput(BaseModel):
    name: str
    balance: float
    transactions: int
    is_active: bool

@app.post("/risk-assessment")
def risk_assessment(customer: CustomerInput):
    return analyse_customer_structured({
        "name": customer.name,
        "balance": customer.balance,
        "transactions": customer.transactions,
        "is_active": customer.is_active
    })


class RequirementInput(BaseModel):
    requirement: str

@app.post("/user-stories")
def user_stories(input: RequirementInput):
    return generate_user_story(input.requirement)


class UseCaseInput(BaseModel):
    use_case: str

@app.post("/eu-ai-act")
def eu_ai_act(input: UseCaseInput):
    return check_eu_ai_act(input.use_case)


class TaxonomyInput(BaseModel):
    client_id: str
    client_name: str
    sector: Optional[str] = None
    nace_code: Optional[str] = None
    main_purpose: Optional[str] = None
    sub_purpose: Optional[str] = None
    loan_amount_eur: float
    ghg_scope1_2_tonnes: Optional[float] = None

@app.post("/eu-taxonomy")
def eu_taxonomy(input: TaxonomyInput):
    return assess_taxonomy({
        "client_id": input.client_id,
        "client_name": input.client_name,
        "sector": input.sector,
        "nace_code": input.nace_code,
        "main_purpose": input.main_purpose,
        "sub_purpose": input.sub_purpose,
        "product_type": "Term Loan",
        "country": "Netherlands",
        "annual_turnover_eur": 0,
        "capex_eur": 0,
        "loan_amount_eur": input.loan_amount_eur,
        "reporting_year": 2024,
        "substantial_contribution_objective": "Climate Change Mitigation",
        "revenue_eligible_pct": None,
        "capex_eligible_pct": None,
        "ghg_scope1_2_tonnes": input.ghg_scope1_2_tonnes,
        "minimum_safeguards_compliant": True
    })