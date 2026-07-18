'use client';

import { Button } from "@/components/ui/button";
import { ArrowRight, Zap, BarChart3, Users } from "lucide-react";
import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Navigation */}
      <nav className="flex items-center justify-between px-6 py-4 border-b border-slate-700">
        <div className="text-2xl font-bold text-white flex items-center gap-2">
          <Zap className="w-8 h-8 text-amber-500" />
          GLOBAL X SPARK AI
        </div>
        <div className="flex gap-4">
          <Link href="/login">
            <Button variant="outline">Sign In</Button>
          </Link>
          <Link href="/register">
            <Button className="bg-amber-600 hover:bg-amber-700">Get Started</Button>
          </Link>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="max-w-7xl mx-auto px-6 py-20 text-center">
        <h1 className="text-6xl font-bold text-white mb-6">
          Enterprise AI Business Intelligence
        </h1>
        <p className="text-xl text-slate-300 mb-12 max-w-2xl mx-auto">
          Discover opportunities, research companies, analyze markets, and accelerate revenue
          growth with enterprise-grade AI intelligence.
        </p>
        <Link href="/register">
          <Button size="lg" className="bg-amber-600 hover:bg-amber-700 gap-2">
            Start Free Trial <ArrowRight className="w-4 h-4" />
          </Button>
        </Link>
      </div>

      {/* Features Section */}
      <div className="max-w-7xl mx-auto px-6 py-20">
        <h2 className="text-4xl font-bold text-white mb-12 text-center">Features</h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="bg-slate-800 p-8 rounded-lg border border-slate-700 hover:border-amber-500 transition">
            <BarChart3 className="w-12 h-12 text-amber-500 mb-4" />
            <h3 className="text-xl font-bold text-white mb-2">Market Research</h3>
            <p className="text-slate-400">AI-powered company and market analysis</p>
          </div>
          <div className="bg-slate-800 p-8 rounded-lg border border-slate-700 hover:border-amber-500 transition">
            <Users className="w-12 h-12 text-amber-500 mb-4" />
            <h3 className="text-xl font-bold text-white mb-2">Lead Management</h3>
            <p className="text-slate-400">Prospect tracking and opportunity discovery</p>
          </div>
          <div className="bg-slate-800 p-8 rounded-lg border border-slate-700 hover:border-amber-500 transition">
            <Zap className="w-12 h-12 text-amber-500 mb-4" />
            <h3 className="text-xl font-bold text-white mb-2">Automation</h3>
            <p className="text-slate-400">Business workflows and outreach automation</p>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="border-t border-slate-700 py-8 text-center text-slate-400">
        <p>&copy; 2024 GLOBAL X SPARK AI. All rights reserved.</p>
      </footer>
    </div>
  );
}
