# Download Gem Timeout

Sometimes when running `bundle` or `gem` to fetch gems, we will get a connection timeout error from `https://rubygems.org`, like

```console
$ bundle update
Fetching source index from https://rubygems.org/

Retrying fetcher due to error (2/4): Bundler::HTTPError Could not fetch specs from https://rubygems.org/ due to underlying error <timed out (https://rubygems.org/specs.4.8.gz)>
```
or

```console
$ gem update --system
ERROR:  While executing gem ... (Gem::RemoteFetcher::UnknownHostError)
    timed out (https://rubygems.org/specs.4.8.gz)
```

It's said that `rubygems.org` has issues with IPv6 setup and does not response on any of its IPv6 addresses. A workaround is to lower the priority of IPv6 address for `rubygems.org` so that gem will try IPv4 first.

In `/etc/gai.conf`, add the following line:

```
precedence  2a04:4e42::0/32  5
```
