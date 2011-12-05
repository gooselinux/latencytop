Name:           latencytop
Version:        0.5
Release:        3%{?dist}
Summary:        System latency monitor

Group:          Applications/System
License:        GPLv2
URL:            http://www.latencytop.org/
Source0:        http://www.latencytop.org/download/%{name}-%{version}.tar.gz
Patch0:         latencytop-Makefile-fixes.patch
Patch1:         latencytop-change-error-message.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ncurses-devel glib2-devel gtk2-devel

%description
LatencyTOP is a tool for software developers (both kernel and userspace), aimed
at identifying where in the system latency is happening, and what kind of
operation/action is causing the latency to happen so that the code can be
changed to avoid the worst latency hiccups. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
export CFLAGS="${CFLAGS:-%{optflags}}"
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
#%doc 
%{_sbindir}/latencytop
%{_datadir}/%{name}
%{_mandir}/man8/*


%changelog
* Wed May 26 2010 Michal Schmidt <mschmidt@redhat.com> 0.5-3
- Do not suggest recompiling the kernel in the error message (#596094)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Michal Schmidt <mschmidt@redhat.com> 0.5-1
- Upstream release 0.5, adds GTK based GUI.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 07 2008 Michal Schmidt <mschmidt@redhat.com> - 0.4-2
- Add an upstream patch to update the translation table.

* Thu Apr 24 2008 Michal Schmidt <mschmidt@redhat.com> - 0.4-1
- Upstream release 0.4.

* Wed Feb 20 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-5
- Own the data directory.

* Tue Feb  5 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-4
- Package the translation table too and modify latencytop.c to look for it in
  the correct directory.
 
* Mon Feb  4 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-3
- Dropped the whitespace-changing hunk from latencytop-standard-cflags.patch.

* Fri Feb  1 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-2
- From review comments - removed whitespace in latencytop-standard-cflags.patch

* Thu Jan 31 2008 Michal Schmidt <mschmidt@redhat.com> - 0.3-1
- Initial package for Fedora.
