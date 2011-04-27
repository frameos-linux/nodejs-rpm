Name:           nodejs

Version:        0.4.5
Release:        4%{?dist}

Summary:        Node.js: Evented I/O for V8 JavaScript
Group:          Development/Languages/Other
License:        MIT
URL:             http://nodejs.org/

Source0:        http://nodejs.org/dist/node-v%{version}.tar.bz2

Patch1:         node-v0.4.0-remove-python-shebangs.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gcc-c++ >= 4.1
BuildRequires:  libstdc++-devel
BuildRequires:  python redhat-rpm-config
BuildRequires:  openssl-devel
# For shared libs:
BuildRequires:  v8-devel >= 3.1.8
BuildRequires:  c-ares-devel >= 1.7.4
BuildRequires:  libev-devel
BuildRequires:  pkgconfig

%description
Node's goal is to provide an easy way to build scalable network programs.
Node is similar in design to and influenced by systems like Ruby's Event
Machine or Python's Twisted. Node takes the event model a bit further—it
presents the event loop as a language construct instead of as a library.


%package devel
Summary:        Node.js development files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       python redhat-rpm-config
Requires:       gcc-c++ >= 4.1

%description devel
This package contains files for Node.js addons development and build


%clean
rm -rf %{buildroot}


%prep
%setup -q -n node-v%{version}
%patch1 -p1


%build
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS"
./configure --prefix=%{_prefix} --shared-v8 --shared-cares --shared-libev
%__make %{?_smp_mflags}


%install
%__make DESTDIR=%{buildroot} install


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE
%attr(755,root,root) %{_bindir}/node
%{_mandir}/man1/node.1*


%files devel
%defattr(-,root,root,-)
# Headers
%dir %{_includedir}/node
%{_includedir}/node/*.h
# Pkg-config
%{_prefix}/lib/pkgconfig/nodejs.pc
# Node-waf
%attr(755,root,root) %{_bindir}/node-waf
%dir %{_prefix}/lib/node
%dir %{_prefix}/lib/node/wafadmin
%dir %{_prefix}/lib/node/wafadmin/Tools
%{_prefix}/lib/node/wafadmin/*


%changelog
* Wed Apr 27 2011 Sergio Rubio <rubiojr@frameos.org> - 0.4.5-4
- add dist macro to Release

* Fri Apr 08 2011 Sergio Rubio <rubiojr@frameos.org> - 0.4.5-3
- rebuild

* Thu Apr 07 2011 Sergio Rubio <rubiojr@frameos.org> - 0.4.5-2
- build dep on pkgconfig, not pkg-config
- remove --debug configure flag

* Sun Apr  3 2011 Oleg Efimov <efimovov@gmail.com> - 0.4.5-1
- Update Node.js to v0.4.5
* Wed Mar 30 2011 Oleg Efimov <efimovov@gmail.com> - 0.4.4-1
- Update Node.js to v0.4.4
* Sat Mar  5 2011 Oleg Efimov <efimovov@gmail.com> - 0.4.2-1
- Update Node.js to v0.4.2
* Mon Feb 21 2011 Oleg Efimov <efimovov@gmail.com> - 0.4.1-2
- Add node_g to package
* Mon Feb 21 2011 Oleg Efimov <efimovov@gmail.com> - 0.4.1-1
- Update Node.js to v0.4.1
* Fri Feb 18 2011 Oleg Efimov <efimovov@gmail.com> - 0.4.0-1
- Update Node.js tarball to v0.4.0
* Sun Jan  9 2011 Oleg Efimov <efimovov@gmail.com> - 0.2.6-1
- Update Node.js tarball to v0.2.6
* Wed Nov 17 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.5-1
- Update Node.js tarball to v0.2.5
* Tue Nov  9 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.4-2
- Remove /usr/lib/node/libraries/*.js from package
* Mon Oct 25 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.4-1
- Update Node.js tarball to v0.2.4
* Mon Oct 18 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.3-2
- Fix requires, get this from Alan Gutierrez spec
* Mon Oct  4 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.3-1
- Update Node.js tarball to v0.2.3
* Tue Sep 21 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.2-3
- Remove nodejs-debug, merge into nodejs
* Mon Sep 20 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.2-2
- Final RPM spec for Node v0.2.2
* Sun Sep 19 2010 Oleg Efimov <efimovov@gmail.com> - 0.2.2-1
- First RPM release
- Node.js v0.2.2 included
