# -*- coding: utf-8 -*-
"""
Glance Zero-Query Inspiration Graph Matcher Client
Transforms ambient visual wallpapers and lifestyle imagery into high-converting retail product recommendations without manual search queries.
Zero external dependencies -- Python 3.9+ standard library only.
"""

import math
from typing import Dict, Any, List

class GlanceZeroQueryInspirationGraphMatcher:
    """
    Replaces reactive search queries with inspiration-driven graph matching,
    balancing visual harmony with Thompson Sampling multi-armed bandit exploration.
    """

    def __init__(self, exploration_temperature: float = 0.25):
        self.temp = exploration_temperature

    def calculate_euclidean_distance(self, vec_a: List[float], vec_b: List[float]) -> float:
        """Calculates normalized Euclidean distance between feature vectors."""
        n = min(len(vec_a), len(vec_b))
        if n == 0: return 1.0
        dist = math.sqrt(sum((vec_a[i] - vec_b[i]) ** 2 for i in range(n)))
        return dist / math.sqrt(n)

    def calculate_trend_velocity_multiplier(self, recent_impressions_24h: int, baseline_impressions_7d: int) -> float:
        """
        Calculates sudden trend burst acceleration.
        """
        hourly_baseline = max(1.0, baseline_impressions_7d / (7.0 * 24.0))
        hourly_recent = max(1.0, recent_impressions_24h / 24.0)
        ratio = hourly_recent / hourly_baseline
        # Dampen logarithmic multiplier
        return min(2.5, max(0.8, 1.0 + 0.3 * math.log(max(1.0, ratio))))

    def match_inspiration_to_products(
        self,
        ambient_visual_features: Dict[str, Any],
        user_history_priors: Dict[str, float] = None,
        product_catalog: List[Dict[str, Any]] = None,
        max_recommendations: int = 4
    ) -> Dict[str, Any]:
        """
        Matches ambient wallpaper aesthetic features to retail catalog SKUs.
        """
        if user_history_priors is None:
            user_history_priors = {"aesthetic_affinity": 0.75, "price_elasticity": 0.50}

        if product_catalog is None:
            product_catalog = [
                {
                    "sku": "GLC-SKU-881",
                    "title": "Minimalist Ceramic Arc Floor Lamp",
                    "category": "Home Design",
                    "aesthetic_vibe": "Nordic Warmth",
                    "feature_vector": [0.82, 0.45, 0.15, 0.90],
                    "impressions_24h": 4200,
                    "impressions_7d": 18000,
                    "base_cvr": 0.042,
                    "price_usd": 380.0
                },
                {
                    "sku": "GLC-SKU-992",
                    "title": "Cashmere Oversized Mockneck Knit",
                    "category": "Luxury Fashion",
                    "aesthetic_vibe": "Quiet Luxury",
                    "feature_vector": [0.78, 0.55, 0.20, 0.85],
                    "impressions_24h": 12500,
                    "impressions_7d": 32000,
                    "base_cvr": 0.058,
                    "price_usd": 690.0
                },
                {
                    "sku": "GLC-SKU-314",
                    "title": "Handcrafted Obsidian Pour-Over Coffee Set",
                    "category": "Artisan Lifestyle",
                    "aesthetic_vibe": "Wabi-Sabi",
                    "feature_vector": [0.35, 0.88, 0.80, 0.40],
                    "impressions_24h": 1800,
                    "impressions_7d": 14000,
                    "base_cvr": 0.035,
                    "price_usd": 145.0
                },
                {
                    "sku": "GLC-SKU-520",
                    "title": "Modular Brushed Aluminum Bookshelf",
                    "category": "Home Design",
                    "aesthetic_vibe": "Industrial Modern",
                    "feature_vector": [0.20, 0.30, 0.95, 0.60],
                    "impressions_24h": 3100,
                    "impressions_7d": 21000,
                    "base_cvr": 0.029,
                    "price_usd": 850.0
                },
                {
                    "sku": "GLC-SKU-777",
                    "title": "Organic Botanical Hydrating Elixir",
                    "category": "Beauty & Wellness",
                    "aesthetic_vibe": "Earthy Minimalist",
                    "feature_vector": [0.65, 0.60, 0.40, 0.70],
                    "impressions_24h": 9800,
                    "impressions_7d": 38000,
                    "base_cvr": 0.064,
                    "price_usd": 95.0
                }
            ]

        target_vector = ambient_visual_features.get("scene_feature_vector", [0.75, 0.50, 0.25, 0.80])
        scene_vibe = ambient_visual_features.get("scene_dominant_vibe", "Modern Warmth")

        scored_candidates = []
        for prod in product_catalog:
            # 1. Visual feature distance match
            dist = self.calculate_euclidean_distance(target_vector, prod.get("feature_vector", []))
            visual_sim = max(0.0, 1.0 - dist)

            # 2. Trend velocity acceleration
            trend_mult = self.calculate_trend_velocity_multiplier(
                prod.get("impressions_24h", 1000),
                prod.get("impressions_7d", 7000)
            )

            # 3. Exploration perturbation (Bandit Exploration)
            exploration_bonus = (math.sin(hash(prod["sku"]) % 100) + 1.0) * 0.5 * self.temp

            # 4. Final Graph Match Propensity Score
            match_score = (0.50 * visual_sim + 0.30 * (prod.get("base_cvr", 0.03) * 10.0) + 0.20 * (trend_mult - 1.0)) + exploration_bonus
            match_score = max(0.0, min(1.0, match_score))

            scored_candidates.append({
                "sku": prod["sku"],
                "title": prod["title"],
                "category": prod["category"],
                "aesthetic_vibe": prod["aesthetic_vibe"],
                "price_usd": prod["price_usd"],
                "match_propensity_pct": round(match_score * 100.0, 1),
                "visual_similarity_score": round(visual_sim, 4),
                "trend_velocity_multiplier": round(trend_mult, 3)
            })

        # Rank by match propensity
        scored_candidates.sort(key=lambda x: x["match_propensity_pct"], reverse=True)
        top_matches = scored_candidates[:max_recommendations]

        avg_confidence = sum(m["match_propensity_pct"] for m in top_matches) / max(1, len(top_matches))

        return {
            "ambient_scene_vibe": scene_vibe,
            "inspiration_confidence_score": round(avg_confidence, 1),
            "match_verdict": "STRONG_DISCOVERY_FIT" if avg_confidence >= 75 else ("MODERATE_FIT" if avg_confidence >= 55 else "EXPLORATORY"),
            "exploration_temperature": self.temp,
            "recommended_catalog_skus": top_matches
        }
