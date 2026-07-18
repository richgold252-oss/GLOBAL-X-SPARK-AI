'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import Link from 'next/link';
import { Zap } from 'lucide-react';

export default function RegisterPage() {
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
    fullName: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    setLoading(true);

    try {
      // API call would go here
      console.log('Register:', formData);
      // Redirect on success
      router.push('/dashboard');
    } catch (err) {
      setError('Registration failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center p-4">
      <Card className="w-full max-w-md bg-slate-800 border-slate-700">
        <CardHeader className="text-center">
          <div className="flex justify-center mb-4">
            <Zap className="w-8 h-8 text-amber-500" />
          </div>
          <CardTitle className="text-white">Create Account</CardTitle>
          <CardDescription>Join GLOBAL X SPARK AI today</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-3">
            {error && <div className="text-red-500 text-sm">{error}</div>}
            <div className="space-y-2">
              <label className="text-sm font-medium text-slate-200">Full Name</label>
              <Input
                type="text"
                name="fullName"
                placeholder="John Doe"
                value={formData.fullName}
                onChange={handleChange}
                className="bg-slate-700 border-slate-600 text-white"
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium text-slate-200">Email</label>
              <Input
                type="email"
                name="email"
                placeholder="you@example.com"
                value={formData.email}
                onChange={handleChange}
                className="bg-slate-700 border-slate-600 text-white"
                required
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium text-slate-200">Username</label>
              <Input
                type="text"
                name="username"
                placeholder="johndoe"
                value={formData.username}
                onChange={handleChange}
                className="bg-slate-700 border-slate-600 text-white"
                required
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium text-slate-200">Password</label>
              <Input
                type="password"
                name="password"
                placeholder="••••••••"
                value={formData.password}
                onChange={handleChange}
                className="bg-slate-700 border-slate-600 text-white"
                required
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-medium text-slate-200">Confirm Password</label>
              <Input
                type="password"
                name="confirmPassword"
                placeholder="••••••••"
                value={formData.confirmPassword}
                onChange={handleChange}
                className="bg-slate-700 border-slate-600 text-white"
                required
              />
            </div>
            <Button
              type="submit"
              disabled={loading}
              className="w-full bg-amber-600 hover:bg-amber-700"
            >
              {loading ? 'Creating account...' : 'Create Account'}
            </Button>
          </form>
          <p className="text-center text-sm text-slate-400 mt-4">
            Already have an account?{' '}
            <Link href="/login" className="text-amber-500 hover:text-amber-400">
              Sign in
            </Link>
          </p>
        </CardContent>
      </Card>
    </div>
  );
}
