'use client';

import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { BarChart3, LogOut, Settings, Users } from 'lucide-react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function DashboardPage() {
  const router = useRouter();

  const handleLogout = () => {
    router.push('/');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <header className="border-b border-slate-700 bg-slate-800/50">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-white">Dashboard</h1>
          <Button variant="outline" onClick={handleLogout} className="gap-2">
            <LogOut className="w-4 h-4" />
            Logout
          </Button>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-6 py-12">
        <div className="mb-12">
          <h2 className="text-4xl font-bold text-white mb-2">Welcome back!</h2>
          <p className="text-slate-400">Here's what's happening with your business today.</p>
        </div>

        <div className="grid md:grid-cols-4 gap-6 mb-12">
          <Card className="bg-slate-800 border-slate-700">
            <CardHeader className="pb-2">
              <CardTitle className="text-sm text-slate-400">Total Companies</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-white">0</div>
            </CardContent>
          </Card>
          <Card className="bg-slate-800 border-slate-700">
            <CardHeader className="pb-2">
              <CardTitle className="text-sm text-slate-400">Total Prospects</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-white">0</div>
            </CardContent>
          </Card>
          <Card className="bg-slate-800 border-slate-700">
            <CardHeader className="pb-2">
              <CardTitle className="text-sm text-slate-400">Reports Generated</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-white">0</div>
            </CardContent>
          </Card>
          <Card className="bg-slate-800 border-slate-700">
            <CardHeader className="pb-2">
              <CardTitle className="text-sm text-slate-400">Team Members</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-white">1</div>
            </CardContent>
          </Card>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          <Card className="bg-slate-800 border-slate-700 hover:border-amber-500 transition cursor-pointer">
            <CardHeader>
              <BarChart3 className="w-8 h-8 text-amber-500 mb-2" />
              <CardTitle className="text-white">Research Companies</CardTitle>
              <CardDescription>Analyze market opportunities</CardDescription>
            </CardHeader>
            <CardContent>
              <Link href="#">
                <Button variant="outline" className="w-full">Get Started</Button>
              </Link>
            </CardContent>
          </Card>
          <Card className="bg-slate-800 border-slate-700 hover:border-amber-500 transition cursor-pointer">
            <CardHeader>
              <Users className="w-8 h-8 text-amber-500 mb-2" />
              <CardTitle className="text-white">Manage Prospects</CardTitle>
              <CardDescription>Track opportunities</CardDescription>
            </CardHeader>
            <CardContent>
              <Link href="#">
                <Button variant="outline" className="w-full">Get Started</Button>
              </Link>
            </CardContent>
          </Card>
          <Card className="bg-slate-800 border-slate-700 hover:border-amber-500 transition cursor-pointer">
            <CardHeader>
              <Settings className="w-8 h-8 text-amber-500 mb-2" />
              <CardTitle className="text-white">Settings</CardTitle>
              <CardDescription>Configure your workspace</CardDescription>
            </CardHeader>
            <CardContent>
              <Link href="#">
                <Button variant="outline" className="w-full">Configure</Button>
              </Link>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
}
