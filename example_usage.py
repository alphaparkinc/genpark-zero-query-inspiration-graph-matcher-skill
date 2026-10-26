# -*- coding: utf-8 -*-
"""
Example usage of GlanceZeroQueryInspirationGraphMatcher
Demonstrates zero-query visual match across ambient lock-screen backgrounds.
"""

from client import GlanceZeroQueryInspirationGraphMatcher

def main():
    matcher = GlanceZeroQueryInspirationGraphMatcher(exploration_temperature=0.20)

    scenes = [
        {
            "name": "Scene 1: Sunlit Minimalist Scandinavian Living Room",
            "features": {
                "scene_dominant_vibe": "Warm Scandinavian Minimalism",
                "scene_feature_vector": [0.80, 0.48, 0.18, 0.88]
            }
        },
        {
            "name": "Scene 2: Moody Industrial Loft Espresso Bar",
            "features": {
                "scene_dominant_vibe": "Industrial Wabi-Sabi",
                "scene_feature_vector": [0.30, 0.85, 0.78, 0.45]
            }
        }
    ]

    print("================================================================")
    print("Glance Zero-Query Inspiration Graph Matcher - Live Runs")
    print("================================================================\n")

    for sc in scenes:
        res = matcher.match_inspiration_to_products(sc["features"], max_recommendations=3)
        print(f"[{sc['name']}]")
        print(f"  Dominant Vibe          : {res['ambient_scene_vibe']}")
        print(f"  Inspiration Confidence : {res['inspiration_confidence_score']}% ({res['match_verdict']})")
        print("  Top Curated Product Matches:")
        for prod in res["recommended_catalog_skus"]:
            print(f"    * [{prod['sku']}] {prod['title']:<40} | ${prod['price_usd']:>6.2f} | Match: {prod['match_propensity_pct']}% (Sim: {prod['visual_similarity_score']}, TrendBurst: {prod['trend_velocity_multiplier']}x)")
        print()

if __name__ == "__main__":
    main()
